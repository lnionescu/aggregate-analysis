import matplotlib.pyplot as plt
from matplotlib.patches import Circle
from matplotlib.collections import PatchCollection
import numpy as np
from aggregate_detector import detect_aggregates
from cellpose_runner import run_cellpose_segmentation
from cellpose import plot
from skimage import io
import scipy.stats as stats
import pandas as pd
import os

def cells_with_foci(brightfield_img, fluorescent_img):
    
    # get cell masks from brightfield image
    #print("Segmenting")
    cell_masks = run_cellpose_segmentation(brightfield_img)

    # detect aggregates in the fluorescent image
    #print("Detecting")
    fluorescent_img, tophat, aggregate_coords = detect_aggregates(fluorescent_img)

    # keep track of which cell IDs contain aggregates
    cells_with_aggregates = []

    # for each aggregate coordinate, check which cell mask it falls within
    for y,x in aggregate_coords:
        cell_id = cell_masks[y,x]
        if cell_id > 0:    # ie not background - this shouldn't happen anyway but just in case
            cells_with_aggregates.append(cell_id)

    #print(f"Found {len(cells_with_aggregates)} cells containing aggregates out of {len(np.unique(cell_masks)) - 1} total cells")


    return cells_with_aggregates, cell_masks, fluorescent_img


def visualize_results(cell_masks, cells_with_aggregates, fluorescent_img):
    # create mask for cells with aggregates
    agg_mask = np.isin(cell_masks, cells_with_aggregates)

    # show fluorescent image with this mask on top
    plt.figure()
    plt.imshow(fluorescent_img)
    plt.contour(agg_mask, colors='yellow', linewidths=1.5)
    plt.title(f"Cells with aggregates: {len(cells_with_aggregates)}")
    plt.axis("off")
    plt.show()
    return 0

def calculate_information_entropy(pixel_values, bins=50):
    """
    Calculate the information entropy of pixel intensity distribution
    
    Parameters:
    - pixel_values: array of pixel intensities
    - bins: number of bins for histogram (default: 50)
    
    Returns:
    - entropy: information entropy in bits
    - hist: histogram counts
    - bin_edges: histogram bin edges
    """
    # Calculate histogram
    hist, bin_edges = np.histogram(pixel_values, bins=bins)
    
    # Remove zero counts to avoid log(0)
    hist = hist[hist > 0]
    
    # Calculate probabilities
    probabilities = hist / np.sum(hist)
    
    # Calculate information entropy: H = -Σ(p * log2(p))
    entropy = -np.sum(probabilities * np.log2(probabilities))
    
    return entropy, hist, bin_edges

def get_hardcoded_image_paths():
    '''
    returns: list of tuples (brightfield_path, fluorescent_path, day, variant, series)
    '''
    # base path to the entire z_projection_results folder
    base_path = '/Users/nataliaionescu/Documents/PKM2/z_projection_results'

    # hardcoded image file paths
    image_paths = [
        # Day 0 (log phase) - nd2_log folder
        (f'{base_path}/nd2_log/E3Q_Series1_Zsum_brightfield.png', f'{base_path}/nd2_log/E3Q_Series1_Zsum_fluorescent.png', 0, 'E3Q', 'Series1'),
        (f'{base_path}/nd2_log/E3Q_Series2_Zsum_brightfield.png', f'{base_path}/nd2_log/E3Q_Series2_Zsum_fluorescent.png', 0, 'E3Q', 'Series2'),
        (f'{base_path}/nd2_log/E3Q_Series3_Zsum_brightfield.png', f'{base_path}/nd2_log/E3Q_Series3_Zsum_fluorescent.png', 0, 'E3Q', 'Series3'),
        (f'{base_path}/nd2_log/E3Q_Series4_Zsum_brightfield.png', f'{base_path}/nd2_log/E3Q_Series4_Zsum_fluorescent.png', 0, 'E3Q', 'Series4'),

        (f'{base_path}/nd2_log/Q10E_Series1_Zsum_brightfield.png', f'{base_path}/nd2_log/Q10E_Series1_Zsum_fluorescent.png', 0, 'Q10E', 'Series1'),
        (f'{base_path}/nd2_log/Q10E_Series2_Zsum_brightfield.png', f'{base_path}/nd2_log/Q10E_Series2_Zsum_fluorescent.png', 0, 'Q10E', 'Series2'),
        (f'{base_path}/nd2_log/Q10E_Series3_Zsum_brightfield.png', f'{base_path}/nd2_log/Q10E_Series3_Zsum_fluorescent.png', 0, 'Q10E', 'Series3'),
        (f'{base_path}/nd2_log/Q10E_Series4_Zsum_brightfield.png', f'{base_path}/nd2_log/Q10E_Series4_Zsum_fluorescent.png', 0, 'Q10E', 'Series4'),

        (f'{base_path}/nd2_log/WT_Series1_Zsum_brightfield.png', f'{base_path}/nd2_log/WT_Series1_Zsum_fluorescent.png', 0, 'WT', 'Series1'),
        (f'{base_path}/nd2_log/WT_Series2_Zsum_brightfield.png', f'{base_path}/nd2_log/WT_Series2_Zsum_fluorescent.png', 0, 'WT', 'Series2'),
        (f'{base_path}/nd2_log/WT_Series3_Zsum_brightfield.png', f'{base_path}/nd2_log/WT_Series3_Zsum_fluorescent.png', 0, 'WT', 'Series3'),
        (f'{base_path}/nd2_log/WT_Series4_Zsum_brightfield.png', f'{base_path}/nd2_log/WT_Series4_Zsum_fluorescent.png', 0, 'WT', 'Series4'),

        # Day 1 - nd2_day1 folder
        (f'{base_path}/nd2_day1/E3Q_Series1_Zsum_brightfield.png', f'{base_path}/nd2_day1/E3Q_Series1_Zsum_fluorescent.png', 1, 'E3Q', 'Series1'),
        (f'{base_path}/nd2_day1/E3Q_Series2_Zsum_brightfield.png', f'{base_path}/nd2_day1/E3Q_Series2_Zsum_fluorescent.png', 1, 'E3Q', 'Series2'),
        (f'{base_path}/nd2_day1/E3Q_Series3_Zsum_brightfield.png', f'{base_path}/nd2_day1/E3Q_Series3_Zsum_fluorescent.png', 1, 'E3Q', 'Series3'),
        (f'{base_path}/nd2_day1/E3Q_Series4_Zsum_brightfield.png', f'{base_path}/nd2_day1/E3Q_Series4_Zsum_fluorescent.png', 1, 'E3Q', 'Series4'),

        (f'{base_path}/nd2_day1/Q10E_Series1_Zsum_brightfield.png', f'{base_path}/nd2_day1/Q10E_Series1_Zsum_fluorescent.png', 1, 'Q10E', 'Series1'),
        (f'{base_path}/nd2_day1/Q10E_Series2_Zsum_brightfield.png', f'{base_path}/nd2_day1/Q10E_Series2_Zsum_fluorescent.png', 1, 'Q10E', 'Series2'),
        (f'{base_path}/nd2_day1/Q10E_Series3_Zsum_brightfield.png', f'{base_path}/nd2_day1/Q10E_Series3_Zsum_fluorescent.png', 1, 'Q10E', 'Series3'),
        (f'{base_path}/nd2_day1/Q10E_Series4_Zsum_brightfield.png', f'{base_path}/nd2_day1/Q10E_Series4_Zsum_fluorescent.png', 1, 'Q10E', 'Series4'),

        (f'{base_path}/nd2_day1/WT_Series1_Zsum_brightfield.png', f'{base_path}/nd2_day1/WT_Series1_Zsum_fluorescent.png', 1, 'WT', 'Series1'),
        (f'{base_path}/nd2_day1/WT_Series2_Zsum_brightfield.png', f'{base_path}/nd2_day1/WT_Series2_Zsum_fluorescent.png', 1, 'WT', 'Series2'),
        (f'{base_path}/nd2_day1/WT_Series3_Zsum_brightfield.png', f'{base_path}/nd2_day1/WT_Series3_Zsum_fluorescent.png', 1, 'WT', 'Series3'),
        (f'{base_path}/nd2_day1/WT_Series4_Zsum_brightfield.png', f'{base_path}/nd2_day1/WT_Series4_Zsum_fluorescent.png', 1, 'WT', 'Series4'),

        # Day 2 - nd2_day2 folder
        (f'{base_path}/nd2_day2/E3Q_Series1_Zsum_brightfield.png', f'{base_path}/nd2_day2/E3Q_Series1_Zsum_fluorescent.png', 2, 'E3Q', 'Series1'),
        (f'{base_path}/nd2_day2/E3Q_Series2_Zsum_brightfield.png', f'{base_path}/nd2_day2/E3Q_Series2_Zsum_fluorescent.png', 2, 'E3Q', 'Series2'),
        (f'{base_path}/nd2_day2/E3Q_Series3_Zsum_brightfield.png', f'{base_path}/nd2_day2/E3Q_Series3_Zsum_fluorescent.png', 2, 'E3Q', 'Series3'),
        (f'{base_path}/nd2_day2/E3Q_Series4_Zsum_brightfield.png', f'{base_path}/nd2_day2/E3Q_Series4_Zsum_fluorescent.png', 2, 'E3Q', 'Series4'),

        (f'{base_path}/nd2_day2/Q10E_Series1_Zsum_brightfield.png', f'{base_path}/nd2_day2/Q10E_Series1_Zsum_fluorescent.png', 2, 'Q10E', 'Series1'),
        (f'{base_path}/nd2_day2/Q10E_Series2_Zsum_brightfield.png', f'{base_path}/nd2_day2/Q10E_Series2_Zsum_fluorescent.png', 2, 'Q10E', 'Series2'),
        (f'{base_path}/nd2_day2/Q10E_Series3_Zsum_brightfield.png', f'{base_path}/nd2_day2/Q10E_Series3_Zsum_fluorescent.png', 2, 'Q10E', 'Series3'),
        (f'{base_path}/nd2_day2/Q10E_Series4_Zsum_brightfield.png', f'{base_path}/nd2_day2/Q10E_Series4_Zsum_fluorescent.png', 2, 'Q10E', 'Series4'),

        (f'{base_path}/nd2_day2/WT_Series1_Zsum_brightfield.png', f'{base_path}/nd2_day2/WT_Series1_Zsum_fluorescent.png', 2, 'WT', 'Series1'),
        (f'{base_path}/nd2_day2/WT_Series2_Zsum_brightfield.png', f'{base_path}/nd2_day2/WT_Series2_Zsum_fluorescent.png', 2, 'WT', 'Series2'),
        (f'{base_path}/nd2_day2/WT_Series3_Zsum_brightfield.png', f'{base_path}/nd2_day2/WT_Series3_Zsum_fluorescent.png', 2, 'WT', 'Series3'),
        (f'{base_path}/nd2_day2/WT_Series4_Zsum_brightfield.png', f'{base_path}/nd2_day2/WT_Series4_Zsum_fluorescent.png', 2, 'WT', 'Series4'),

        # Day 3 - nd2_day3 folder
        (f'{base_path}/nd2_day3/E3Q_Series1_Zsum_brightfield.png', f'{base_path}/nd2_day3/E3Q_Series1_Zsum_fluorescent.png', 3, 'E3Q', 'Series1'),
        (f'{base_path}/nd2_day3/E3Q_Series2_Zsum_brightfield.png', f'{base_path}/nd2_day3/E3Q_Series2_Zsum_fluorescent.png', 3, 'E3Q', 'Series2'),
        (f'{base_path}/nd2_day3/E3Q_Series3_Zsum_brightfield.png', f'{base_path}/nd2_day3/E3Q_Series3_Zsum_fluorescent.png', 3, 'E3Q', 'Series3'),
        (f'{base_path}/nd2_day3/E3Q_Series4_Zsum_brightfield.png', f'{base_path}/nd2_day3/E3Q_Series4_Zsum_fluorescent.png', 3, 'E3Q', 'Series4'),

        (f'{base_path}/nd2_day3/Q10E_Series1_Zsum_brightfield.png', f'{base_path}/nd2_day3/Q10E_Series1_Zsum_fluorescent.png', 3, 'Q10E', 'Series1'),
        (f'{base_path}/nd2_day3/Q10E_Series2_Zsum_brightfield.png', f'{base_path}/nd2_day3/Q10E_Series2_Zsum_fluorescent.png', 3, 'Q10E', 'Series2'),
        (f'{base_path}/nd2_day3/Q10E_Series3_Zsum_brightfield.png', f'{base_path}/nd2_day3/Q10E_Series3_Zsum_fluorescent.png', 3, 'Q10E', 'Series3'),
        (f'{base_path}/nd2_day3/Q10E_Series4_Zsum_brightfield.png', f'{base_path}/nd2_day3/Q10E_Series4_Zsum_fluorescent.png', 3, 'Q10E', 'Series4'),

        (f'{base_path}/nd2_day3/WT_Series1_Zsum_brightfield.png', f'{base_path}/nd2_day3/WT_Series1_Zsum_fluorescent.png', 3, 'WT', 'Series1'),
        (f'{base_path}/nd2_day3/WT_Series2_Zsum_brightfield.png', f'{base_path}/nd2_day3/WT_Series2_Zsum_fluorescent.png', 3, 'WT', 'Series2'),
        (f'{base_path}/nd2_day3/WT_Series3_Zsum_brightfield.png', f'{base_path}/nd2_day3/WT_Series3_Zsum_fluorescent.png', 3, 'WT', 'Series3'),
        (f'{base_path}/nd2_day3/WT_Series4_Zsum_brightfield.png', f'{base_path}/nd2_day3/WT_Series4_Zsum_fluorescent.png', 3, 'WT', 'Series4'),
    ]

    return image_paths

def calculate_cell_entropies_from_image_pair(brightfield_path, fluorescent_path, bins=50):
    '''
    for a brightfield/fluorescent image pair, bins intensities within each cell and calculates entropy, then returns a list of all cell entropies
    '''
    brightfield_img = io.imread(brightfield_path)
    fluorescent_img = io.imread(fluorescent_path)

    # get cell masks
    cell_masks = run_cellpose_segmentation(brightfield_img)

    # calculate entropy for each cell
    cell_entropies = []
    unique_cells = np.unique(cell_masks)

    # loop over identified cells
    for cell_id in unique_cells:
        if cell_id == 0:  # skip background
            continue

        # get fluorescent pixels for this cell
        cell_pixels = fluorescent_img[cell_masks == cell_id]

        if len(cell_pixels) > 0:
            entropy, _, _ = calculate_information_entropy(cell_pixels, bins=bins)
            cell_entropies.append(entropy)

    return cell_entropies

def process_all_conditions(bins=50):
    '''
    process all image pairs and calculate entropies
    returns: df with columns: day, variant, series, cell_entropy
    '''
    image_paths = get_hardcoded_image_paths()
    results = []

    print(f"Processing {len(image_paths)} image pairs...")

    for brightfield_path, fluorescent_path, day, variant, series in image_paths:
        print(f"Processing: {variant} Day {day} {series}")

        # calculate entropies for this image pair
        entropies = calculate_cell_entropies_from_image_pair(brightfield_path, fluorescent_path, bins)

        # add each cell's entropy to results
        for entropy in entropies:
            results.append({
                'day': day,
                'variant': variant,
                'series': series,
                'cell_entropy': entropy
            })

        print(f"  → {len(entropies)} cells")

    return pd.DataFrame(results)

def calculate_pooled_confidence_intervals(df, confidence=0.95):
    """
    Calculate confidence intervals by pooling all cells across all 4 series
    for each day+variant combination
    
    Parameters:
    - df: DataFrame with columns day, variant, series, cell_entropy
    - confidence: confidence level (default 0.95)
    
    Returns:
    - DataFrame with day, variant, mean_entropy, lower_ci, upper_ci, n_cells
    """
    results = []
    
    # Get unique day+variant combinations
    for day in sorted(df['day'].unique()):
        for variant in df['variant'].unique():
            
            # Get ALL cells for this day+variant (pooled across all series)
            mask = (df['day'] == day) & (df['variant'] == variant)
            pooled_data = df[mask]['cell_entropy']
            
            if len(pooled_data) > 0:
                mean = pooled_data.mean()
                sem = stats.sem(pooled_data)  # Standard error of the mean
                
                # Use t-distribution with df = n_cells - 1
                t_value = stats.t.ppf((1 + confidence) / 2, len(pooled_data) - 1)
                ci = t_value * sem
                
                results.append({
                    'day': day,
                    'variant': variant,
                    'mean_entropy': mean,
                    'lower_ci': mean - ci,
                    'upper_ci': mean + ci,
                    'n_cells': len(pooled_data)
                })
    
    return pd.DataFrame(results)

def plot_entropy_results_with_anova(df, confidence=0.95):
    """
    Plot entropy results with confidence intervals and ANOVA p-values
    
    Parameters:
    - df: DataFrame from process_all_conditions
    - confidence: confidence level for error bars
    
    Returns:
    - summary_df: DataFrame with statistics
    """
    from scipy import stats
    
    # Calculate summary statistics
    summary_df = calculate_pooled_confidence_intervals(df, confidence)
    
    variants = sorted(df['variant'].unique())
    days = sorted(df['day'].unique())
    colors = ['blue', 'orange', 'green']
    
    plt.figure(figsize=(12, 8))
    
    # Plot each variant
    for i, variant in enumerate(variants):
        variant_data = summary_df[summary_df['variant'] == variant]
        
        if len(variant_data) > 0:
            x = variant_data['day']
            y = variant_data['mean_entropy']
            errors = [y - variant_data['lower_ci'], variant_data['upper_ci'] - y]
            
            plt.errorbar(x, y, yerr=errors, fmt='o-', 
                        color=colors[i], label=variant, 
                        capsize=5, linewidth=2, markersize=8)
    
    # Calculate ANOVA for each day and add significance markers
    y_max = plt.ylim()[1]
    y_text = y_max * 0.95
    
    for day in days:
        # Get data for all variants on this day
        day_data = []
        for variant in variants:
            variant_day_data = df[(df['day'] == day) & (df['variant'] == variant)]['cell_entropy']
            if len(variant_day_data) > 0:
                day_data.append(variant_day_data.values)
        
        # Perform ANOVA if we have data for at least 2 variants
        if len(day_data) >= 2:
            f_stat, p_value = stats.f_oneway(*day_data)
            
            # Determine significance level
            if p_value < 0.001:
                sig_text = "***"
            elif p_value < 0.01:
                sig_text = "**"
            elif p_value < 0.05:
                sig_text = "*"
            else:
                sig_text = "ns"
            
            # Add significance marker above the plot
            plt.text(day, y_text, sig_text, ha='center', va='center', 
                    fontsize=14, fontweight='bold',
                    bbox=dict(boxstyle="round,pad=0.3", facecolor="white", alpha=0.8))
            
            # Add p-value below the significance marker
            if p_value < 0.001:
                p_text = "p=0.000"
            else:
                p_text = f"p={p_value:.3f}"
            
            plt.text(day, y_text * 0.88, p_text, ha='center', va='center', 
                    fontsize=10, style='italic')
    
    plt.xlabel('Day')
    plt.ylabel('Information Entropy (bits)')
    plt.title(f'Cell Information Entropy Over Time\n(Significance markers: *** p<0.001, ** p<0.01, * p<0.05, ns = not significant)')
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.show()
    
    # Print ANOVA results
    print("\nANOVA Results:")
    print("-" * 40)
    for day in days:
        day_data = []
        for variant in variants:
            variant_day_data = df[(df['day'] == day) & (df['variant'] == variant)]['cell_entropy']
            if len(variant_day_data) > 0:
                day_data.append(variant_day_data.values)
        
        if len(day_data) >= 2:
            f_stat, p_value = stats.f_oneway(*day_data)
            if p_value < 0.05:
                interpretation = "Variants ARE significantly different"
            else:
                interpretation = "Variants are similar (not significantly different)"
            print(f"Day {day}: F={f_stat:.3f}, p={p_value:.4f} - {interpretation}")
        else:
            print(f"Day {day}: Not enough data for ANOVA")
    
    return summary_df


def save_results(df, summary_df, output_dir="entropy_results"):
    """
    Save results to CSV files
    """
    os.makedirs(output_dir, exist_ok=True)
    
    # Save full results
    df.to_csv(os.path.join(output_dir, "all_cell_entropies.csv"), index=False)
    
    # Save summary statistics
    summary_df.to_csv(os.path.join(output_dir, "entropy_summary_stats.csv"), index=False)
    
    print(f"Results saved to {output_dir}/")

def main(bins=50, confidence=0.95, save_output=True):
    """
    Main function to run the complete entropy analysis
    """
    print("Starting entropy analysis...")
    print("="*60)
    
    # Process all conditions
    df = process_all_conditions(bins=bins)
    
    if df.empty:
        print("No data found. Please check your image paths.")
        return None, None
    
    print(f"\nSuccessfully processed {len(df)} cells")
    
    # Print summary
    print("\nData summary:")
    print("-" * 40)
    for variant in sorted(df['variant'].unique()):
        for day in sorted(df['day'].unique()):
            n_cells = len(df[(df['variant'] == variant) & (df['day'] == day)])
            if n_cells > 0:
                print(f"  {variant} Day {day}: {n_cells} cells")
    
    # Create plot with ANOVA
    print("\nCreating plot with statistical analysis...")
    summary_df = plot_entropy_results_with_anova(df, confidence=confidence)
    
    # Save results
    if save_output:
        save_results(df, summary_df)
    
    print("\nFinal Summary:")
    print("=" * 60)
    print(summary_df.to_string(index=False))
    
    return df, summary_df

# Run the analysis
if __name__ == "__main__":
    df, summary_df = main(bins=50, confidence=0.95, save_output=True)




