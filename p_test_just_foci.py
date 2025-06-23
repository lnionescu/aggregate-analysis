import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import os
from pathlib import Path

def load_and_process_data():
    """
    Load all CSV files using hardcoded paths and organize the data
    """
    # Hardcoded file paths
    file_paths = [
        # Day 0 (log phase)
        ('/Users/nataliaionescu/Documents/PKM2/z_projection_results/nd2_log/E3Q_Series1_Zsum_fluorescent_cell_measurements.csv', 0, 'E3Q', 'Series1'),
        ('/Users/nataliaionescu/Documents/PKM2/z_projection_results/nd2_log/Q10E_Series1_Zsum_fluorescent_cell_measurements.csv', 0, 'Q10E', 'Series1'),
        ('/Users/nataliaionescu/Documents/PKM2/z_projection_results/nd2_log/WT_Series1_Zsum_fluorescent_cell_measurements.csv', 0, 'WT', 'Series1'),
        ('/Users/nataliaionescu/Documents/PKM2/z_projection_results/nd2_log/E3Q_Series2_Zsum_fluorescent_cell_measurements.csv', 0, 'E3Q', 'Series2'),
        ('/Users/nataliaionescu/Documents/PKM2/z_projection_results/nd2_log/Q10E_Series2_Zsum_fluorescent_cell_measurements.csv', 0, 'Q10E', 'Series2'),
        ('/Users/nataliaionescu/Documents/PKM2/z_projection_results/nd2_log/WT_Series2_Zsum_fluorescent_cell_measurements.csv', 0, 'WT', 'Series2'),
        ('/Users/nataliaionescu/Documents/PKM2/z_projection_results/nd2_log/E3Q_Series3_Zsum_fluorescent_cell_measurements.csv', 0, 'E3Q', 'Series3'),
        ('/Users/nataliaionescu/Documents/PKM2/z_projection_results/nd2_log/Q10E_Series3_Zsum_fluorescent_cell_measurements.csv', 0, 'Q10E', 'Series3'),
        ('/Users/nataliaionescu/Documents/PKM2/z_projection_results/nd2_log/WT_Series3_Zsum_fluorescent_cell_measurements.csv', 0, 'WT', 'Series3'),
        ('/Users/nataliaionescu/Documents/PKM2/z_projection_results/nd2_log/E3Q_Series4_Zsum_fluorescent_cell_measurements.csv', 0, 'E3Q', 'Series4'),
        ('/Users/nataliaionescu/Documents/PKM2/z_projection_results/nd2_log/Q10E_Series4_Zsum_fluorescent_cell_measurements.csv', 0, 'Q10E', 'Series4'),
        ('/Users/nataliaionescu/Documents/PKM2/z_projection_results/nd2_log/WT_Series4_Zsum_fluorescent_cell_measurements.csv', 0, 'WT', 'Series4'),
        
        # Day 1
        ('/Users/nataliaionescu/Documents/PKM2/z_projection_results/nd2_day1/E3Q_Series1_Zsum_fluorescent_cell_measurements.csv', 1, 'E3Q', 'Series1'),
        ('/Users/nataliaionescu/Documents/PKM2/z_projection_results/nd2_day1/Q10E_Series1_Zsum_fluorescent_cell_measurements.csv', 1, 'Q10E', 'Series1'),
        ('/Users/nataliaionescu/Documents/PKM2/z_projection_results/nd2_day1/WT_Series1_Zsum_fluorescent_cell_measurements.csv', 1, 'WT', 'Series1'),
        ('/Users/nataliaionescu/Documents/PKM2/z_projection_results/nd2_day1/E3Q_Series2_Zsum_fluorescent_cell_measurements.csv', 1, 'E3Q', 'Series2'),
        ('/Users/nataliaionescu/Documents/PKM2/z_projection_results/nd2_day1/Q10E_Series2_Zsum_fluorescent_cell_measurements.csv', 1, 'Q10E', 'Series2'),
        ('/Users/nataliaionescu/Documents/PKM2/z_projection_results/nd2_day1/WT_Series2_Zsum_fluorescent_cell_measurements.csv', 1, 'WT', 'Series2'),
        ('/Users/nataliaionescu/Documents/PKM2/z_projection_results/nd2_day1/E3Q_Series3_Zsum_fluorescent_cell_measurements.csv', 1, 'E3Q', 'Series3'),
        ('/Users/nataliaionescu/Documents/PKM2/z_projection_results/nd2_day1/Q10E_Series3_Zsum_fluorescent_cell_measurements.csv', 1, 'Q10E', 'Series3'),
        ('/Users/nataliaionescu/Documents/PKM2/z_projection_results/nd2_day1/WT_Series3_Zsum_fluorescent_cell_measurements.csv', 1, 'WT', 'Series3'),
        ('/Users/nataliaionescu/Documents/PKM2/z_projection_results/nd2_day1/E3Q_Series4_Zsum_fluorescent_cell_measurements.csv', 1, 'E3Q', 'Series4'),
        ('/Users/nataliaionescu/Documents/PKM2/z_projection_results/nd2_day1/Q10E_Series4_Zsum_fluorescent_cell_measurements.csv', 1, 'Q10E', 'Series4'),
        ('/Users/nataliaionescu/Documents/PKM2/z_projection_results/nd2_day1/WT_Series4_Zsum_fluorescent_cell_measurements.csv', 1, 'WT', 'Series4'),
        
        # Day 2
        ('/Users/nataliaionescu/Documents/PKM2/z_projection_results/nd2_day2/E3Q_Series1_Zsum_fluorescent_cell_measurements.csv', 2, 'E3Q', 'Series1'),
        ('/Users/nataliaionescu/Documents/PKM2/z_projection_results/nd2_day2/Q10E_Series1_Zsum_fluorescent_cell_measurements.csv', 2, 'Q10E', 'Series1'),
        ('/Users/nataliaionescu/Documents/PKM2/z_projection_results/nd2_day2/WT_Series1_Zsum_fluorescent_cell_measurements.csv', 2, 'WT', 'Series1'),
        ('/Users/nataliaionescu/Documents/PKM2/z_projection_results/nd2_day2/E3Q_Series2_Zsum_fluorescent_cell_measurements.csv', 2, 'E3Q', 'Series2'),
        ('/Users/nataliaionescu/Documents/PKM2/z_projection_results/nd2_day2/Q10E_Series2_Zsum_fluorescent_cell_measurements.csv', 2, 'Q10E', 'Series2'),
        ('/Users/nataliaionescu/Documents/PKM2/z_projection_results/nd2_day2/WT_Series2_Zsum_fluorescent_cell_measurements.csv', 2, 'WT', 'Series2'),
        ('/Users/nataliaionescu/Documents/PKM2/z_projection_results/nd2_day2/E3Q_Series3_Zsum_fluorescent_cell_measurements.csv', 2, 'E3Q', 'Series3'),
        ('/Users/nataliaionescu/Documents/PKM2/z_projection_results/nd2_day2/Q10E_Series3_Zsum_fluorescent_cell_measurements.csv', 2, 'Q10E', 'Series3'),
        ('/Users/nataliaionescu/Documents/PKM2/z_projection_results/nd2_day2/WT_Series3_Zsum_fluorescent_cell_measurements.csv', 2, 'WT', 'Series3'),
        ('/Users/nataliaionescu/Documents/PKM2/z_projection_results/nd2_day2/E3Q_Series4_Zsum_fluorescent_cell_measurements.csv', 2, 'E3Q', 'Series4'),
        ('/Users/nataliaionescu/Documents/PKM2/z_projection_results/nd2_day2/Q10E_Series4_Zsum_fluorescent_cell_measurements.csv', 2, 'Q10E', 'Series4'),
        ('/Users/nataliaionescu/Documents/PKM2/z_projection_results/nd2_day2/WT_Series4_Zsum_fluorescent_cell_measurements.csv', 2, 'WT', 'Series4'),
        
        # Day 3
        ('/Users/nataliaionescu/Documents/PKM2/z_projection_results/nd2_day3/E3Q_Series1_Zsum_fluorescent_cell_measurements.csv', 3, 'E3Q', 'Series1'),
        ('/Users/nataliaionescu/Documents/PKM2/z_projection_results/nd2_day3/Q10E_Series1_Zsum_fluorescent_cell_measurements.csv', 3, 'Q10E', 'Series1'),
        ('/Users/nataliaionescu/Documents/PKM2/z_projection_results/nd2_day3/WT_Series1_Zsum_fluorescent_cell_measurements.csv', 3, 'WT', 'Series1'),
        ('/Users/nataliaionescu/Documents/PKM2/z_projection_results/nd2_day3/E3Q_Series2_Zsum_fluorescent_cell_measurements.csv', 3, 'E3Q', 'Series2'),
        ('/Users/nataliaionescu/Documents/PKM2/z_projection_results/nd2_day3/Q10E_Series2_Zsum_fluorescent_cell_measurements.csv', 3, 'Q10E', 'Series2'),
        ('/Users/nataliaionescu/Documents/PKM2/z_projection_results/nd2_day3/WT_Series2_Zsum_fluorescent_cell_measurements.csv', 3, 'WT', 'Series2'),
        ('/Users/nataliaionescu/Documents/PKM2/z_projection_results/nd2_day3/E3Q_Series3_Zsum_fluorescent_cell_measurements.csv', 3, 'E3Q', 'Series3'),
        ('/Users/nataliaionescu/Documents/PKM2/z_projection_results/nd2_day3/Q10E_Series3_Zsum_fluorescent_cell_measurements.csv', 3, 'Q10E', 'Series3'),
        ('/Users/nataliaionescu/Documents/PKM2/z_projection_results/nd2_day3/WT_Series3_Zsum_fluorescent_cell_measurements.csv', 3, 'WT', 'Series3'),
        ('/Users/nataliaionescu/Documents/PKM2/z_projection_results/nd2_day3/E3Q_Series4_Zsum_fluorescent_cell_measurements.csv', 3, 'E3Q', 'Series4'),
        ('/Users/nataliaionescu/Documents/PKM2/z_projection_results/nd2_day3/Q10E_Series4_Zsum_fluorescent_cell_measurements.csv', 3, 'Q10E', 'Series4'),
        ('/Users/nataliaionescu/Documents/PKM2/z_projection_results/nd2_day3/WT_Series4_Zsum_fluorescent_cell_measurements.csv', 3, 'WT', 'Series4'),
    ]
    
    data = []
    
    for filepath, day, variant, series in file_paths:
        if os.path.exists(filepath):
            try:
                df = pd.read_csv(filepath)
                
                # Check if required columns exist
                required_cols = ['has_aggregate', 'cell_mean_intensity']
                if not all(col in df.columns for col in required_cols):
                    print(f"Warning: Missing required columns in {filepath}")
                    continue
                
                # Add metadata to each row
                df['day'] = day
                df['variant'] = variant
                df['series'] = series
                df['file_path'] = filepath
                
                data.append(df)
                print(f"Loaded: {os.path.basename(filepath)} ({len(df)} cells)")
                
            except Exception as e:
                print(f"Error loading {filepath}: {e}")
                continue
        else:
            print(f"File not found: {filepath}")
    
    if not data:
        raise ValueError("No data files found! Check your file paths.")
    
    # Combine all data
    combined_df = pd.concat(data, ignore_index=True)
    print(f"\nTotal data loaded: {len(combined_df)} cells from {len(data)} files")
    
    return combined_df

def calculate_mean_intensity(df, has_foci=True, intensity_type='cell'):
    """
    Calculate mean intensity for cells with or without foci
    intensity_type: 'cell' for cell intensity, 'foci' for aggregate intensity
    """
    if has_foci:
        if intensity_type == 'foci':
            # For foci intensity - use aggregate_mean_intensity
            if 'aggregate_mean_intensity' in df.columns:
                return df['aggregate_mean_intensity']
            else:
                print("Warning: 'aggregate_mean_intensity' not found!")
                return pd.Series(dtype=float)
        else:
            # Cells with foci - use rest_of_cell_mean_intensity if available, otherwise cell_mean_intensity
            if 'rest_of_cell_mean_intensity' in df.columns:
                return df['rest_of_cell_mean_intensity']
            else:
                print("Warning: 'rest_of_cell_mean_intensity' not found, using 'cell_mean_intensity'")
                return df['cell_mean_intensity']
    else:
        # Cells without foci - use cell_mean_intensity
        return df['cell_mean_intensity']

def simple_anova_for_plot(df, has_foci, days, intensity_type='cell'):
    """
    Simple ANOVA test for one cell type (with or without foci)
    Returns significance results for each day
    intensity_type: 'cell' for cell intensity, 'foci' for aggregate intensity
    """
    from scipy import stats
    
    variants = ['E3Q', 'Q10E', 'WT']
    results = {}
    
    for day in days:
        # Get data for each variant on this day
        variant_data = []
        
        for variant in variants:
            mask = (df['variant'] == variant) & (df['day'] == day) & (df['has_aggregate'] == has_foci)
            subset = df[mask]
            
            if len(subset) > 0:
                intensities = calculate_mean_intensity(subset, has_foci, intensity_type)
                intensities = intensities.dropna()
                if len(intensities) > 0:
                    variant_data.append(intensities.values)
        
        # Do ANOVA if we have data for at least 2 variants
        if len(variant_data) >= 2:
            f_stat, p_value = stats.f_oneway(*variant_data)
            
            if p_value < 0.001:
                sig_text = "***"
            elif p_value < 0.01:
                sig_text = "**"
            elif p_value < 0.05:
                sig_text = "*"
            else:
                sig_text = "ns"
                
            results[day] = {'p_value': p_value, 'significance': sig_text}
        else:
            results[day] = {'p_value': None, 'significance': 'n/a'}
    
    return results

def plot_cell_intensities(df):
    """
    Create plots showing mean intensities over time for cells with and without foci
    WITH ANOVA results shown on each plot
    """
    variants = ['E3Q', 'Q10E', 'WT']
    colors = ['blue', 'orange', 'green']
    
    # Create plots for three different intensity types
    plot_types = [
        (True, 'WITH Foci (Cell)', 'Mean Intensity (excluding foci)', [1, 2, 3], 'cell'),
        (False, 'WITHOUT Foci', 'Mean Intensity', [0, 1, 2, 3], 'cell'),
        (True, 'FOCI ONLY', 'Mean Foci Intensity', [1, 2, 3], 'foci')
    ]
    
    for has_foci, title_suffix, ylabel, days, intensity_type in plot_types:
        plt.figure(figsize=(12, 7))
        
        # Run ANOVA for this plot type
        anova_results = simple_anova_for_plot(df, has_foci, days, intensity_type)
        
        for variant_idx, variant in enumerate(variants):
            means = []
            errors = []
            
            for day in days:
                # Filter data for this variant, day, and foci status
                mask = (df['variant'] == variant) & (df['day'] == day) & (df['has_aggregate'] == has_foci)
                subset = df[mask]
                
                if len(subset) > 0:
                    intensities = calculate_mean_intensity(subset, has_foci, intensity_type)
                    intensities = intensities.dropna()  # Remove NaN values
                    
                    if len(intensities) > 0:
                        mean_val = intensities.mean()
                        std_err = intensities.std() / np.sqrt(len(intensities))  # Standard error
                        means.append(mean_val)
                        errors.append(std_err * 1.96)  # 95% confidence interval
                    else:
                        means.append(np.nan)
                        errors.append(np.nan)
                else:
                    means.append(np.nan)
                    errors.append(np.nan)
            
            # Plot the data
            plt.errorbar(days, means, yerr=errors, 
                        fmt='o-', color=colors[variant_idx], label=variant,
                        capsize=5, linewidth=2, markersize=8)
        
        # Add ANOVA significance markers above the plot
        y_max = plt.ylim()[1]
        y_text = y_max * 0.95
        
        for day in days:
            if day in anova_results and anova_results[day]['significance'] != 'n/a':
                sig_text = anova_results[day]['significance']
                p_val = anova_results[day]['p_value']
                
                # Add significance marker
                plt.text(day, y_text, sig_text, ha='center', va='top', 
                        fontsize=14, fontweight='bold',
                        bbox=dict(boxstyle="round,pad=0.3", facecolor="white", alpha=0.8))
                
                # Add p-value below the marker
                plt.text(day, y_text * 0.85, f'p={p_val:.3f}', ha='center', va='top', 
                        fontsize=10, style='italic')
        
        plt.xlabel('Day')
        plt.ylabel(ylabel)
        plt.title(f'{title_suffix}\n(Significance markers: *** p<0.001, ** p<0.01, * p<0.05, ns = not significant)')
        plt.legend()
        plt.grid(True, alpha=0.3)
        plt.tight_layout()
        plt.show()
        
        # Print ANOVA results for this plot type
        print(f"\nANOVA Results for {title_suffix}:")
        print("-" * 40)
        for day in days:
            if day in anova_results and anova_results[day]['p_value'] is not None:
                p_val = anova_results[day]['p_value']
                sig = anova_results[day]['significance']
                if p_val < 0.05:
                    interpretation = "Variants ARE significantly different"
                else:
                    interpretation = "Variants are similar (not significantly different)"
                print(f"Day {day}: p={p_val:.4f} ({sig}) - {interpretation}")
            else:
                print(f"Day {day}: Not enough data for ANOVA")
        print()

def print_summary_stats(df):
    """
    Print summary statistics
    """
    print("\n" + "="*50)
    print("SUMMARY STATISTICS")
    print("="*50)
    
    for variant in df['variant'].unique():
        print(f"\n{variant}:")
        variant_data = df[df['variant'] == variant]
        
        for day in sorted(df['day'].unique()):
            day_data = variant_data[variant_data['day'] == day]
            
            if len(day_data) > 0:
                with_foci = day_data[day_data['has_aggregate'] == True]
                without_foci = day_data[day_data['has_aggregate'] == False]
                
                print(f"  Day {day}: {len(day_data)} total cells, "
                      f"{len(with_foci)} with foci ({len(with_foci)/len(day_data)*100:.1f}%), "
                      f"{len(without_foci)} without foci ({len(without_foci)/len(day_data)*100:.1f}%)")

# Main execution
def main():
    try:
        # Load all data
        print("Loading data...")
        df = load_and_process_data()
        
        # Print summary statistics
        print_summary_stats(df)
        
        # Create plots
        print("\nCreating plots...")
        plot_cell_intensities(df)
        
        print("\nAnalysis complete!")
        
    except Exception as e:
        print(f"Error: {e}")
        print("\nTroubleshooting tips:")
        print("1. Check that your file paths are correct")
        print("2. Make sure your CSV files exist")
        print("3. Verify your CSV files have the required columns: 'has_aggregate', 'cell_mean_intensity'")

if __name__ == "__main__":
    main()
