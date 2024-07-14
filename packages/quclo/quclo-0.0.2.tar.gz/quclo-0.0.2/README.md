# QuClo CLI

QuClo CLI is a command-line interface tool designed to simplify the execution and management of quantum circuits across multiple backend providers. This tool leverages the QuClo platform to offer a seamless experience for researchers, educators, and hobbyists in quantum computing.

## Features

- **Execute Quantum Circuits:** Run your quantum circuits on various backend providers.
- **Intelligent Backend Selection:** Choose the best backend based on criteria like cost, speed, fidelity, and queue time.
- **Result Visualization:** Generate comprehensive and easy-to-understand visualizations of your quantum circuit results.
- **Open-Source SDK Integration:** Easily integrate and submit circuits created with other SDKs.

## Installation

To install the QuClo CLI, ensure you have Python installed, then use pip:

```bash
pip install quclo
```

## Usage

CLI:

```bash
quclo --help
```

UI:

```bash
pip install pdoc
pdoc quclo --logo https://quclo.com/assets/quclo-Cg4oDc2h.svg
```

1. Create a new user account:

   ```bash
   quclo user create
   ```

2. Authenticate with your user account:

   ```bash
   quclo user login
   ```

3. List available backend:

   ```bash
   quclo backend list
   ```

4. Display details of a specific backend:

   ```bash
   quclo backend show ibmq_qasm_simulator
   ```

5. Execute a quantum circuit:

   **Using priority:**

   ```bash
   quclo circuit run --priority cost "include 'stdgates.inc'; qubit[1] q;'
   ```

   **Using backend:**

   ```bash
   quclo circuit run --backend ibmq_qasm_simulator 'include "stdgates.inc"; qubit[1] q;'
   ```

6. Get the status and results of a quantum circuit:

   ```bash
   quclo circuit status 1
   ```

   ```bash
    quclo circuit result 1
   ```

## Contributing

Contributions are welcome! Please submit a pull request or open an issue to discuss any changes.

## Contact

For any questions or feedback, please contact us at [support@quclo.com](mailto:support@quclo.com).
