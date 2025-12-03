import pandas as pd
import numpy as np
import os
def generate_tuned_dataset(num_samples=2000, output_file='rtl_dataset.csv'):
    print(f"Generating {num_samples} synthetic circuit samples...")
    data = []
    for _ in range(num_samples):
        if np.random.rand() > 0.5:
            nodes = int(np.random.normal(15, 5))
            depth = int(np.random.normal(7, 2))
            fanout = int(np.random.normal(2, 1))
        else:
            nodes = int(np.random.normal(50, 20))
            depth = int(np.random.normal(12, 4))
            fanout = int(np.random.normal(4, 2))
        nodes = max(2, nodes)
        depth = max(2, depth)
        fanout = max(1, fanout)
        base_delay = (depth * 0.35) + (fanout * 0.1) + (nodes * 0.01)
        noise = np.random.normal(0, 0.05)
        total_delay_ns = base_delay + noise
        data.append([nodes, depth, fanout, round(total_delay_ns, 4)])
    df = pd.DataFrame(data, columns=['Nodes', 'Logic_Depth', 'Fan_Out', 'Timing_Delay_ns'])
    df.to_csv(output_file, index=False)
    print(f"Dataset saved to {output_file}")
    return df
if __name__ == "__main__":
    generate_tuned_dataset()