# DevOps Provisioning Simulator

This project simulates the provisioning of infrastructure components using Python and Bash scripts.  
It demonstrates user input handling, service installation logic, logging, and system automation.

The project is designed to run on Linux systems and includes clean modular Python design, structured logging, and Bash provisioning scripts.

## Objectives
- Simulate provisioning flow using Python & Bash
- Demonstrate modular coding structure
- Implement logging for both Python and Bash
- Showcase error handling and automation logic

 ### Setup Instructions 📌

1. Install requirements (ONLY NEEDED IF RUNNING WINDOWS):
Install Python interpreter (Can be found at the official site: https://www.python.org/downloads/ )
Install Git Bash / GUI (Can be found at the official site: https://git-scm.com/install/ )
After installing these, open CMD and execute.

2. Clone the repository:
git clone https://github.com/MikyMaor/DevOpsProject.git
cd DevOpsProject

3. Create Python Virtual Environment:
open CMD and execute >
python -m venv venv
./venv/Scripts/activate
pip install pydantic

4. Set or Verify bash file permissions (X):
chmod +x scripts/install_service_nginx.sh

5. Run the project:
python Infra_simulator.py


#### Expected Output
- User chooses services
- Python logs provisioning steps
- Bash scripts install selected services
- Log file generated: logs/provisioning.log


##### EXAMPLE #####

$ python Infra_simulator.py

Enter Machine Name (or 'done' to finish): web-server-01
Enter OS (Windows/Linux): Linux
Enter CPU (e.g. Intel Core XXX, AMD Ryzen XXX): Intel Core i5
Enter RAM Capacity (e.g. 4GB): 8GB

🔧 Running installation script at: /home/user/DevOpsProject/scripts/install_service_nginx.sh
--- Bash Script Output ---
Nginx installed successfully!

✔ Machine added.

Enter Machine Name (or 'done' to finish): done

✔ Saved to configs/instances.json