from tsunami_ip_utils.readers import read_integral_indices
from tsunami_ip_utils.integral_indices import calculate_E
import numpy as np
from uncertainties import unumpy
import pandas as pd
from pandas import DataFrame as df
from pathlib import Path
from tsunami_ip_utils.perturbations import generate_points
from typing import List, Dict, Tuple, Any
from tsunami_ip_utils.viz.scatter_plot import EnhancedPlotlyFigure
from tsunami_ip_utils.viz.plot_utils import generate_plot_objects_array_from_perturbations, generate_plot_objects_from_array_contributions
from tsunami_ip_utils.integral_indices import get_uncertainty_contributions, calculate_E_contributions
from tsunami_ip_utils.viz import matrix_plot
import inspect

def comparison(tsunami_ip_output_filename: Path, application_filenames: List[Path], 
               experiment_filenames: List[Path]) -> Dict[str, df]:
    """Function that compares the calculated similarity parameter E with the TSUNAMI-IP output for each application with each
    experiment. The comparison is done for the nominal values and the uncertainties of the E values. In addition, the
    difference between manually calculated uncertainties and automatically calculated uncertainties (i.e. via the uncertainties
    package) is also calculated. The results are returned as a pandas DataFrame.
    
    Parameters
    ----------
    tsunami_ip_output_filename
        Path to the TSUNAMI-IP output file.
    application_filenames
        Paths to the application sdf files.
    experiment_filenames
        Paths to the experiment sdf files.
    
    Returns
    -------
        Dictionary of pandas DataFrames for each type of E index. The DataFrames contain the calculated E values,
        the manual uncertainties, the TSUNAMI-IP values, the relative difference in the mean, and the relative difference
        in the manual uncertainty. The DataFrames are indexed by the experiment number and the columns are a MultiIndex
        with the application number as the main index and the attributes as the subindex."""
    
    # First perform the manual calculations for each type of E index
    E_types = ['total', 'fission', 'capture', 'scatter']
    E = {}
    for E_type in E_types + ['total_manual', 'fission_manual', 'capture_manual', 'scatter_manual']:
        if 'manual' in E_type: # Manual uncertainty propagation
            if E_type.replace('_manual', '') == 'total':
                E[E_type] = calculate_E(application_filenames, experiment_filenames, reaction_type='all', uncertainties='manual')
            elif E_type.replace('_manual', '') == 'scatter':
                E[E_type] = calculate_E(application_filenames, experiment_filenames, reaction_type='elastic', uncertainties='manual')
            else:
                E[E_type] = calculate_E(application_filenames, experiment_filenames, reaction_type=E_type.replace('_manual', ''), uncertainties='manual')
        else: # Automatic uncertainty propagation
            if E_type == 'total':
                E[E_type] = calculate_E(application_filenames, experiment_filenames, reaction_type='all')
            elif E_type == 'scatter':
                E[E_type] = calculate_E(application_filenames, experiment_filenames, reaction_type='elastic')
            else:
                E[E_type] = calculate_E(application_filenames, experiment_filenames, reaction_type=E_type)

    print("Done with calculations")

    # Now read the tsunami_ip output
    tsunami_ip_output = read_integral_indices(tsunami_ip_output_filename)

    # Compare the nominal values
    E_diff = {}
    for E_type in E_types:
        E_diff[E_type] = np.abs(unumpy.nominal_values(E[E_type]) - unumpy.nominal_values(tsunami_ip_output[f"E_{E_type}"])) \
                            / unumpy.nominal_values(tsunami_ip_output[f"E_{E_type}"])

    # Compare the calculated (manual) uncertainty with the TSUNAMI-IP uncertainty
    E_diff_unc = {}
    for E_type in E_types:
        E_diff_unc[E_type] = np.abs( unumpy.std_devs(E[E_type + '_manual']) - unumpy.std_devs(tsunami_ip_output[f"E_{E_type}"]) ) \
                                / unumpy.std_devs(tsunami_ip_output[f"E_{E_type}"])

    # -----------------------------------------
    # Format the results as a pandas DataFrame
    # -----------------------------------------

    # Create a MultiIndex for columns
    num_experiments, num_applications = np.shape(E['total'])

    columns = pd.MultiIndex.from_product([
        np.arange(1, num_applications + 1),  # Main column indices
        ['Calculated', 'Manual Uncertainty', 'TSUNAMI-IP', 'Relative Difference in Mean', 'Relative Difference in Manual Uncertainty']  # Subcolumns
    ], names=['Application Number', 'Attribute'])

    # Initialize DataFrame
    data = {}

    print("Creating pandas dataframes")

    # Create a pandas DataFrame for each type of E index
    for E_type in E_types:
        data[E_type] = pd.DataFrame(index=pd.Index(np.arange(1, num_experiments + 1), name='Experiment Number'), columns=columns)

        # Populate DataFrame
        for application_index in range(num_applications):
            for experiment_index in range(num_experiments):
                # Now write the data to the DataFrame
                data[E_type].loc[experiment_index + 1, (application_index + 1, 'Calculated')] = \
                    f"{E[E_type][experiment_index, application_index].n:1.3E}+/-{E[E_type][experiment_index, application_index].s:1.2E}"
                data[E_type].loc[experiment_index + 1, (application_index + 1, 'Manual Uncertainty')] = \
                    f"{E[E_type + '_manual'][experiment_index, application_index].s:1.2E}"
                data[E_type].loc[experiment_index + 1, (application_index + 1, 'TSUNAMI-IP')] = \
                    f"{tsunami_ip_output[f'E_{E_type}'][experiment_index, application_index].n:1.3E}+/-{tsunami_ip_output[f'E_{E_type}'][experiment_index, application_index].s:1.2E}"
                data[E_type].loc[experiment_index + 1, (application_index + 1, 'Relative Difference in Mean')] = f"{E_diff[E_type][experiment_index, application_index]:1.4E}"
                data[E_type].loc[experiment_index + 1, (application_index + 1, 'Relative Difference in Manual Uncertainty')] = f"{E_diff_unc[E_type][experiment_index, application_index]:1.4E}"

    return data

def _update_annotation(fig: EnhancedPlotlyFigure, integral_index: float, index_name: str
                       ) -> Tuple[EnhancedPlotlyFigure, float, float]:
    """Update the annotation on the plot to include the TSUNAMI-IP c_k value and the percent difference from the
    Pearson correlation coefficient. If the percent difference is greater than 5%, the annotation will be colored red.
    
    Parameters
    ----------
    fig
        The plotly figure object.
    integral_index
        The TSUNAMI-IP integral_index value.
    index_name
        The name of the integral index.
        
    Returns
    -------
        * fig
            The plotly figure object with the updated annotation.
        * calculated_value
            The calculated value of the integral index.
        * percent_difference
            The percent difference between the TSUNAMI-IP integral_index value and the Pearson correlation coefficient.
    """
    summary_stats_annotation = fig.layout.annotations[0]
    calculated_value = fig.statistics['pearson']
    percent_difference = (integral_index - calculated_value)/integral_index * 100
    summary_stats_annotation.text += f"<br>TSUNAMI-IP {index_name}: <b>{integral_index}</b><br>Percent Difference: <b>{percent_difference}</b>%"
    
    if percent_difference > 5:
        summary_stats_annotation.update(bordercolor='red')
    return fig,  calculated_value, percent_difference

def correlation_comparison(integral_index_matrix: unumpy.uarray, integral_index_name: str, application_files: List[Path], 
                           experiment_files: List[Path], method: str, base_library: Path=None, perturbation_factors: Path=None, 
                           num_perturbations: int=None) -> Tuple[pd.DataFrame, Any]:
    """Function that compares the calculated similarity parameter C_k (calculated using the cross section sampling method) 
    with the TSUNAMI-IP output for each application and each experiment. NOTE: that the experiment sdfs and application sdfs
    must correspond with those in hte TSUNAMI-IP input file.

    Notes
    -----
    If the chosen method is uncertainty_contributions_nuclide or uncertainty_contributions_nuclide_reaction, the required input
    files are TSUNAMI ``.out`` files. Otherwise, the required input files are TSUNAMI ``.sdf`` files.
    
    Parameters
    ----------
    integral_index_matrix:
        The matrix representing the given integral index. Expected shape is ``(num_applications, num_experiments)``.
    integral_index_name:
        The name of the integral index (used for selecting the method for the plot). Allowed values of ``'c_k'``, ``'E'``.
    application_files
        Paths to the input files for the application (required by the chosen method, either TSUNAMI ``.out`` files or 
        TSUNAMI ``.sdf`` files).
    experiment_files
        Paths to the input files for the experiment (required by the chosen method, either TSUNAMI ``.out`` files or 
        TSUNAMI ``.sdf`` files).
    method
        The method for visualizing the given integral index. Allowed values of ``'perturbation'``, 
        ``'uncertainty_contributions_nuclide'``, ``'uncertainty_contributions_nuclide_reaction'``, 
        ``'E_contributions_nuclide'``, ``'E_contributions_nuclide_reaction'``, ``'c_k_contributions'``. 
    base_library
        Path to the base library
    perturbation_factors
        Path to the perturbation factors.
    num_perturbations
        Number of perturbations to generate.
    
    Returns
    -------
        * comparisons
            A pandas DataFrame containing the calculated integral index values, the TSUNAMI-IP values, and the percent
            difference between the two values.
        * matrix_plot
            The matrix plot object containing the integral index values and the percent difference.
    """

    # ===================================
    # Perform checks on input parameters
    # ===================================

    # Check for consistent dimensions of the integral index matrix
    num_applications, num_experiments = np.shape(integral_index_matrix)
    if num_applications != len(application_files) or num_experiments != len(experiment_files):
        raise ValueError("The dimensions of the integral index matrix do not match the number of applications and experiments.")

    # Check for missing input parameters or inconsistent method
    missing_perturbation_parameters = any([base_library is None, perturbation_factors is None,
                                             num_perturbations is None])
    if method == 'perturbation' and missing_perturbation_parameters:
        raise ValueError("The method is 'perturbation', and some of the required additional parameters are missing.")

    method_for_calculating_c_k = method in ['uncertainty_contributions_nuclide', 'uncertainty_contributions_nuclide_reaction',
                                                'perturbation', 'c_k_contributions']
    method_for_calculating_E = method in ['E_contributions_nuclide', 'E_contributions_nuclide_reaction']
    if integral_index_name == 'c_k' and not method_for_calculating_c_k:
        raise ValueError("The integral index name is 'c_k', but a method for calculating c_k was not selected, instead"
                         f"the method selected was {method}. Please select a method for calculating c_k.")
    if integral_index_name == 'E' and not method_for_calculating_E:
        raise ValueError("The integral index name is 'E', but the method selected was not 'E_contributions'. Please"
                         f"the method selected was {method}. Please select a method for calculating E.")


    # ===================================
    # Generate plots for the matrix plot
    # ===================================
    match method:
        case 'perturbation':
            points_array = generate_points(application_files, experiment_files, base_library, perturbation_factors, 
                                           num_perturbations)
            plot_objects_array = generate_plot_objects_array_from_perturbations(points_array)

        case 'uncertainty_contributions_nuclide':
            contributions_nuclide, _ = get_uncertainty_contributions(application_files, experiment_files)
            plot_objects_array = generate_plot_objects_from_array_contributions(contributions_nuclide, '%Δk/k')

        case 'uncertainty_contributions_nuclide_reaction':
            _, contributions_nuclide_reaction = get_uncertainty_contributions(application_files, experiment_files)
            plot_objects_array = generate_plot_objects_from_array_contributions(contributions_nuclide_reaction, '%Δk/k')

        case 'E_contributions_nuclide':
            contributions_nuclide, _ =  calculate_E_contributions(application_files, experiment_files)
            plot_objects_array = generate_plot_objects_from_array_contributions(contributions_nuclide, 
                                                                                integral_index_name)

        case 'E_contributions_nuclide_reaction':
            _, contributions_nuclide_reaction =  calculate_E_contributions(application_files, experiment_files)
            plot_objects_array = generate_plot_objects_from_array_contributions(contributions_nuclide_reaction, 
                                                                                integral_index_name)

        case 'c_k_contributions':
            raise NotImplementedError("The method 'c_k_contributions' is not yet implemented.")
            # plot_objects_array = generate_plot_objects_from_array_contributions(integral_index_matrix, )

    # ==============================
    # Update plots with annotations
    # ==============================
    percent_differences = np.empty_like(integral_index_matrix)
    calculated_values = np.empty_like(integral_index_matrix)
    for i, row in enumerate(plot_objects_array):
        for j, plot_object in enumerate(row):
            updated_plot_object, calculated_value, percent_difference = \
                _update_annotation(plot_object, integral_index_matrix[i, j], integral_index_name)
            calculated_values[i, j] = calculated_value
            percent_differences[i, j] = percent_difference
            plot_objects_array[i, j] = updated_plot_object

    # ===================================
    # Create dataframes with comparisons
    # ===================================
    num_applications, num_experiments = np.shape(integral_index_matrix)
    columns = pd.MultiIndex.from_product([
        np.arange(1, num_applications + 1),  # Main column indices
        ['Calculated', 'TSUNAMI-IP', 'Percent Difference']  # Subcolumns
    ], names=['Application Number', 'Attribute'])

    comparisons = pd.DataFrame(index=pd.Index(np.arange(1, num_experiments + 1), name='Experiment Number'), columns=columns)
    # Populate DataFrame
    for application_index in range(num_applications):
        for experiment_index in range(num_experiments):
            # Now write the data to the DataFrame
            comparisons.loc[experiment_index + 1, (application_index + 1, 'Calculated')] = \
                f"{calculated_values[experiment_index, application_index]:1.3E}"
            comparisons.loc[experiment_index + 1, (application_index + 1, 'TSUNAMI-IP')] = \
                f"{integral_index_matrix[experiment_index, application_index].n:1.3E}+/-{integral_index_matrix[experiment_index, application_index].s:1.2E}"
            comparisons.loc[experiment_index + 1, (application_index + 1, 'Percent Difference')] = \
                f"{percent_differences[experiment_index, application_index].n:2.2f}+/-{percent_differences[experiment_index, application_index].n:1.2E}"
    
    # ===================
    # Create matrix plot
    # ===================
    fig = matrix_plot(plot_objects_array, 'interactive')

    return comparisons, fig