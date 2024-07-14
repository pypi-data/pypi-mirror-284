import argparse
import os
from .main import (
    analyze_return,
    analyze_overflow_and_return,
    analyze_underflow_and_return,
    analyze_reentrancy,
    check_private_key_exposure,
    analyze_floating_pragma,
    analyze_denial_of_service,
    analyze_unchecked_external_calls,
    analyze_greedy_suicidal_functions,
    print_vulnerabilities,
    save_report,
)

def run_analysis(file_path):
    """
    Analyzes vulnerabilities in Lua code from a specified file.

    Args:
    - file_path (str): Path to the Lua code file.

    """
    with open(file_path, 'r') as file:
        code = file.read()

    analyze_return(code)
    analyze_overflow_and_return(code)
    analyze_underflow_and_return(code)
    analyze_reentrancy(code)
    check_private_key_exposure(code)
    analyze_floating_pragma(code)
    analyze_denial_of_service(code)
    analyze_unchecked_external_calls(code)
    analyze_greedy_suicidal_functions(code)

    print_vulnerabilities()

    report_file_path = "report.json"
    save_report(report_file_path)
    print(f"\nVulnerability report saved to {report_file_path}\n")

def generate_html_report(file_name):
    """
    Generates an HTML report displaying vulnerabilities from 'report.json'.

    Args:
    - file_name (str): Name of the Lua code file for the report title.

    """
    template_html = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title class="text-center font-extrabold text-3xl">Vulnerability Report for {file_name}</title>
        <link href="https://cdn.jsdelivr.net/npm/tailwindcss@2.2.19/dist/tailwind.min.css" rel="stylesheet">
        <style>
            .severity-high {{ color: red; }}
            .severity-medium {{ color: orange; }}
            .severity-low {{ color: green; }}
            body {{ overflow-x: hidden; }} 
        </style>
    </head>
    <body class="bg-gray-100 p-6">
        <div class="w-screen mx-auto bg-white shadow-md rounded-md p-6">
            <h1 class="text-3xl text-center font-extrabold mb-4">Vulnerability Report for {file_name}</h1>
            
            <div class="grid grid-cols-1 md:grid-cols-3 gap-4">
                <div id="highSeverityList" class="space-y-4">
                    <h2 class="text-xl text-center font-bold mb-2 text-red-500">High Severity</h2>
                </div>
                <div id="mediumSeverityList" class="space-y-4">
                    <h2 class="text-xl text-center font-bold mb-2 text-yellow-400">Medium Severity</h2>
                </div>
                <div id="lowSeverityList" class="space-y-4">
                    <h2 class="text-xl text-center  font-bold mb-2 text-green-300">Low Severity</h2>
                </div>
            </div>
        </div>

        <script>
            fetch('report.json')
                .then(response => response.json())
                .then(data => {{
                    const highSeverityList = document.getElementById('highSeverityList');
                    const mediumSeverityList = document.getElementById('mediumSeverityList');
                    const lowSeverityList = document.getElementById('lowSeverityList');

                    data.forEach(vuln => {{
                        const vulnerabilityDiv = document.createElement('div');
                        vulnerabilityDiv.className = 'bg-white rounded-md shadow-md p-4 space-y-2';

                        vulnerabilityDiv.innerHTML = `
                            <h2 class="text-lg font-bold">${{vuln.name}}</h2>
                            <p class="text-gray-600">${{vuln.description}}</p>
                            <div class="flex justify-between">
                                <span class="text-sm font-medium">Pattern: ${{vuln.pattern}}</span>
                            </div>
                            <span class="text-sm text-gray-500">Line: ${{vuln.line}}</span>
                        `;

                        switch (vuln.severity.toLowerCase()) {{
                            case 'high':
                                highSeverityList.appendChild(vulnerabilityDiv);
                                break;
                            case 'medium':
                                mediumSeverityList.appendChild(vulnerabilityDiv);
                                break;
                            case 'low':
                                lowSeverityList.appendChild(vulnerabilityDiv);
                                break;
                        }}
                    }});
                }})
                .catch(error => console.error('Error fetching data:', error));

            function getSeverityClass(severity) {{
                switch (severity.toLowerCase()) {{
                    case 'high':
                        return 'severity-high';
                    case 'medium':
                        return 'severity-medium';
                    case 'low':
                        return 'severity-low';
                    default:
                        return '';
                }}
            }}
        </script>
    </body>
    </html>
    """
    with open('report.html', 'w') as html_file:
        html_file.write(template_html)

    print("\nHTML report generated successfully.\n")

def main():
    """
    Main function to handle command-line arguments and execute vulnerability analysis.

    """
    parser = argparse.ArgumentParser(description="= Vulnerability Analyzer")
    parser.add_argument("file", help="Path to  code file")
    parser.add_argument("--generate-report", action="store_true", help="Generate vulnerability report in HTML")

    args = parser.parse_args()

    if os.path.isfile(args.file):
        print(f"Analyzing file: {args.file}")
        run_analysis(args.file)
        
        if args.generate_report:
            if os.path.isfile("report.json"):
                generate_html_report(os.path.basename(args.file))
            else:
                print("Please generate the report first using '--generate-report' option.")
    else:
        print("File not found. Please enter a valid file path.")

if __name__ == "__main__":
    main()
