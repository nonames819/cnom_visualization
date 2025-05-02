import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm

def visualize_traj(x, y, z, output_path):
    """
    Visualize 3D trajectory with time-gradient coloring and save to file.
    
    Args:
        x (np.ndarray): X coordinates of trajectory
        y (np.ndarray): Y coordinates of trajectory
        z (np.ndarray): Z coordinates of trajectory
        output_path (str): Path to save the visualization (including filename)
        Example usage:
        visualize_traj(
            action[:, 0],
            action[:, 1], 
            action[:, 2],
            'trajectory_visualization.png'
        )
    """
    # Create figure and 3D axis
    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111, projection='3d')

    # Create time-gradient red colormap
    n_points = len(x)
    colors = cm.Reds(np.linspace(0.3, 1, n_points))

    # Plot 3D trajectory
    for i in range(len(x)-1):
        ax.plot(x[i:i+2], y[i:i+2], z[i:i+2], 
                color=colors[i], 
                linewidth=2)

    # Add start and end point markers
    ax.scatter(x[0], y[0], z[0], color='blue', s=100, label='Start')
    ax.scatter(x[-1], y[-1], z[-1], color='green', s=100, label='End')

    # Set axis labels
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')

    # Add title and legend
    ax.set_title('Trajectory Visualization (Red gradient indicates time)')
    ax.legend()

    # Adjust view angle
    ax.view_init(elev=30, azim=45)

    # Save figure
    plt.savefig(output_path, dpi=300, bbox_inches='tight')
    plt.close()

