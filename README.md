
# 📡 Mininet-Floodlight-Pathfinding

This repository contains the files for setting up a custom Software-Defined Networking (SDN) environment using **Mininet** for network emulation and the **Floodlight Controller** for intelligent routing, specifically implementing a **K-shortest path finding** capability.

The core functionality involves a custom Floodlight module that computes multiple optimized routes between any two switches in the network using **Yen's algorithm**, while also managing network partitioning into clusters and archipelagos.


![Python](https://img.shields.io/badge/python-3.8%2B-blue?logo=python&logoColor=white) 
![NumPy](https://img.shields.io/badge/numpy-1.24%2B-013243?logo=numpy&logoColor=white) 
![CVXPY](https://img.shields.io/badge/cvxpy-1.3%2B-green) 
![Matplotlib](https://img.shields.io/badge/Matplotlib-Data_Viz-orange?logo=matplotlib&logoColor=white)


## Description

The project is structured around two main components:
1.  **Network Emulation:** A custom 8-switch, 8-host topology defined in **Mininet** (`topology.py`).
2.  **SDN Control Logic:** A modified Floodlight controller module (`TopologyInstance.java`) that performs advanced topology discovery and path computation.

The Java component uses a highly optimized implementation of Dijkstra's algorithm for finding the shortest path (and broadcast trees) and extends this capability to Yen's algorithm for computing up to **K-shortest paths** (configurable) between any two nodes. An accompanying Python script (`contoller.py`) provides a local simulation of the shortest path using Dijkstra's algorithm for testing graph representations.

## Features

* **Custom Topology:** A dedicated 8-switch, 8-host (`h1-h8` connected to `s1-s8`) network with specific inter-switch links for complex path testing.
* **K-Shortest Path Routing (Yen's Algorithm):** Implements an efficient method to find multiple paths between source and destination switches, which is critical for fault tolerance and load balancing in SDN.
* **Optimized Shortest Path (Dijkstra's Algorithm):** Used as the core subroutine in Yen's algorithm and for computing network broadcast trees.
* **Dynamic Clustering:** Uses a modified Tarjan's algorithm to identify strongly connected components (Clusters and Archipelagos) within the network, enhancing topology management.
* **Simulated Pathfinding:** An independent Python script demonstrates Dijkstra's pathfinding on the same network structure for visualization and testing.

---

## File Descriptions

| File | Type/Module | Description |
| :--- | :--- | :--- |
| `topology.py` | Mininet Topology | Defines the custom `MyTopo` class with 8 switches and 8 hosts, and links configured with `bw=1000, delay='1ms'`. This is the network structure used by Mininet. |
| `TopologyInstance.java` | Floodlight Module | The core Java class for the Floodlight controller. It implements `dijkstra`, a modified Tarjan's clustering, and the `yens` algorithm to compute multiple best paths between switches. |
| `contoller.py` | Python Script | A standalone Python script that defines a `Graph` class and uses Dijkstra's algorithm to find the shortest path between user-specified switches (`s1` to `s8`) using randomly assigned link weights from 1 to 10. |
| `commands.txt` | Shell Commands | Contains the necessary `sudo` commands to clean up Mininet, stop any existing controller processes, and launch the custom topology connected to a remote controller. |

---

## Installation

### Prerequisites

You must have **Mininet** and a **Floodlight controller** (typically the source code for compilation) installed and configured on your system.

### Steps

1.  **Clone the Repository:**
    ```bash
    git clone [your-repository-url]
    cd Mininet-Floodlight-Pathfinding
    ```

2.  **Setup Mininet Topology:**
    Copy the custom topology file into the directory where you will run Mininet (e.g., in your Mininet environment's main folder or a directory accessible by Mininet).
    ```bash
    cp topology.py /path/to/mininet/custom/topos/
    ```

3.  **Integrate Floodlight Module:**
    The `TopologyInstance.java` file needs to be integrated into the Floodlight source code (specifically within the `net.floodlightcontroller.topology` package) and the Floodlight controller must be re-compiled and started.

    * **Place the file:** Place `TopologyInstance.java` into your Floodlight source tree: `floodlight/src/main/java/net/floodlightcontroller/topology/TopologyInstance.java`
    * **Compile and Run Floodlight:** Follow the standard Floodlight build process (e.g., using `ant` and then running the controller).

4.  **Install Python Dependencies:**
    The accompanying Python script requires `NumPy`.
    ```bash
    pip install numpy
    ```
    *(Note: CVXPY and Matplotlib badges are included as required, but are not strictly necessary for the current version of `contoller.py`.)*

---

## Usage

### 1. Start the Network

First, ensure your Floodlight controller is running. Then, execute the Mininet commands from `commands.txt` in your terminal:

```bash
# Clean up previous Mininet sessions
sudo mn -c

# Kill any existing process listening on the default OpenFlow port (6653)
sudo fuser -k 6653/tcp

# Start the custom topology 'mytopo' and connect it to the remote controller
# (Floodlight should be running on the default IP/Port)
sudo mn --custom topology.py --topo mytopo --controller remote
````

Mininet will start, and the switches (`s1` through `s8`) will connect to the running Floodlight controller. The controller will then begin topology discovery and compute the path caches.

### 2\. Run the Python Pathfinding Simulation

You can run the standalone `controller.py` script to simulate the shortest path calculation on the graph structure locally:

```bash
python contoller.py
```

**Example Interaction:**
The script will prompt you for the start and target switch numbers (1 to 8):

```
Type start and target switches: 1 8
We found the following best path with a value of X.
s1 -> s3 -> s8
```

-----

## Contributing

We welcome contributions to enhance this project, particularly to expand the pathfinding metrics in the Floodlight module or integrate the Python pathfinding output with the Mininet environment.

1.  **Report Issues:** Use the GitHub Issues tracker to report bugs or suggest new features.
2.  **Feature Suggestions:** Open an issue to discuss significant changes before starting development.
3.  **Pull Requests:** Fork the repository, create a new branch, commit your changes, and submit a pull request. Please ensure your code follows the existing style and includes relevant documentation/comments.

-----

## License

This project is licensed under the **MIT License**.

## Contact/Support

For questions or support, please open an issue in this repository.

