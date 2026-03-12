Industrial Data Acquisition Gateway (OPC UA)

A high-performance industrial bridge built using the OPC Foundation .NET Standard stack. This project facilitates secure communication between an OPC UA Simulation Server and a .NET-based management layer, optimized for data acquisition and real-time monitoring.
🛠 Project Overview
This repository serves as a technical demonstration of industrial IoT connectivity. It integrates a Python-based simulation bridge with a .NET 8 gateway to handle machine-level data.

Gateway Logic: Custom .NET implementation for session management and node subscription.

Protocol Stack: Built on the official OPC Foundation UA-.NETStandard libraries.

Security: Implements PKI-based application authentication and secure channel establishment.

⚙️ Tech Stack
Languages: C# (.NET 8.0), Python 3.x

Protocol: OPC UA (TCP/Binary)

Core Library: OPC Foundation UA-.NETStandard

Tooling: UAExpert (Client Testing), GitHub Actions (CI/CD ready)

📂 Project Structure
Program.cs: The primary entry point for the .NET Gateway, handling server discovery and data reading.

bridge.py: Python script used for simulating or bridging auxiliary data streams.

*.sln / *.csproj: Refactored project files following industrial naming conventions for NDA compliance.

🚀 Getting Started
1. Prerequisites
.NET 8.0 SDK

Python 3.x

The original stack (already integrated as a dependency): OPC Foundation GitHub

2. Setup & Execution
Start the Server:
Ensure your OPC UA Simulation Server is running (typically on opc.tcp://localhost:48040).

Run the Gateway:
Navigate to this project folder and execute:

Bash
dotnet run
Data Verification:
Use UAExpert to connect to the server and verify that the .NET Gateway is successfully reading and processing the nodes.

💡 Key Technical Challenges Solved
NDA Compliance: Successfully scrubbed internal industrial identifiers while maintaining code integrity.

Asynchronous Integration: Managed data flow between the Python simulation layer and the asynchronous C# task-based gateway.

Certificate Handling: Configured local PKI folders to automatically generate and trust application certificates during runtime.

📜 Acknowledgments
Powered by the OPC Foundation open-source .NET Standard stack.
