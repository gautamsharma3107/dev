"""
Day 8 - Mini Project 3: HTML Report Generator
=============================================
Generate HTML reports from data

This project applies:
- HTML generation
- JSON data processing
- Template patterns
- HTML escaping for security
"""

import json
import html
from datetime import datetime

print("=" * 60)
print("Mini Project 3: HTML Report Generator")
print("=" * 60)

class HTMLReportGenerator:
    """
    Generate HTML reports from various data sources.
    """
    
    def __init__(self, title="Report"):
        self.title = title
        self.styles = self._default_styles()
    
    def _default_styles(self):
        """Return default CSS styles"""
        return """
        <style>
            * { margin: 0; padding: 0; box-sizing: border-box; }
            body {
                font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, sans-serif;
                line-height: 1.6;
                color: #333;
                background: #f5f5f5;
                padding: 20px;
            }
            .container { max-width: 1200px; margin: 0 auto; }
            .report {
                background: white;
                border-radius: 8px;
                box-shadow: 0 2px 10px rgba(0,0,0,0.1);
                padding: 30px;
                margin-bottom: 20px;
            }
            h1 {
                color: #2c3e50;
                border-bottom: 3px solid #3498db;
                padding-bottom: 10px;
                margin-bottom: 20px;
            }
            h2 { color: #34495e; margin: 20px 0 10px; }
            h3 { color: #7f8c8d; margin: 15px 0 10px; }
            table {
                width: 100%;
                border-collapse: collapse;
                margin: 15px 0;
            }
            th, td {
                border: 1px solid #ddd;
                padding: 12px;
                text-align: left;
            }
            th {
                background: #3498db;
                color: white;
            }
            tr:nth-child(even) { background: #f9f9f9; }
            tr:hover { background: #f5f5f5; }
            .card {
                background: #fff;
                border: 1px solid #e1e1e1;
                border-radius: 8px;
                padding: 20px;
                margin: 15px 0;
            }
            .card-grid {
                display: grid;
                grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
                gap: 20px;
            }
            .stat-box {
                text-align: center;
                padding: 20px;
                background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                color: white;
                border-radius: 8px;
            }
            .stat-box .number { font-size: 2.5em; font-weight: bold; }
            .stat-box .label { opacity: 0.9; }
            .badge {
                display: inline-block;
                padding: 4px 12px;
                border-radius: 20px;
                font-size: 0.85em;
                font-weight: 500;
            }
            .badge-success { background: #2ecc71; color: white; }
            .badge-warning { background: #f39c12; color: white; }
            .badge-danger { background: #e74c3c; color: white; }
            .badge-info { background: #3498db; color: white; }
            .footer {
                text-align: center;
                color: #999;
                padding: 20px;
                font-size: 0.9em;
            }
            .chart-bar {
                display: flex;
                align-items: center;
                margin: 8px 0;
            }
            .chart-bar-label { width: 150px; }
            .chart-bar-bg {
                flex: 1;
                height: 25px;
                background: #ecf0f1;
                border-radius: 4px;
                overflow: hidden;
            }
            .chart-bar-fill {
                height: 100%;
                background: linear-gradient(90deg, #3498db, #2ecc71);
                transition: width 0.3s;
            }
            .chart-bar-value { width: 60px; text-align: right; }
        </style>
        """
    
    def _escape(self, text):
        """Safely escape HTML"""
        return html.escape(str(text)) if text else ""
    
    def _generate_header(self):
        """Generate HTML header"""
        return f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{self._escape(self.title)}</title>
    {self.styles}
</head>
<body>
<div class="container">
"""
    
    def _generate_footer(self):
        """Generate HTML footer"""
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        return f"""
    <div class="footer">
        Generated on {timestamp} by HTML Report Generator
    </div>
</div>
</body>
</html>
"""
    
    def generate_table(self, headers, rows, title=None):
        """Generate an HTML table"""
        html_str = ""
        if title:
            html_str += f"<h3>{self._escape(title)}</h3>\n"
        
        html_str += "<table>\n<thead>\n<tr>\n"
        for header in headers:
            html_str += f"  <th>{self._escape(header)}</th>\n"
        html_str += "</tr>\n</thead>\n<tbody>\n"
        
        for row in rows:
            html_str += "<tr>\n"
            for cell in row:
                html_str += f"  <td>{self._escape(cell)}</td>\n"
            html_str += "</tr>\n"
        
        html_str += "</tbody>\n</table>\n"
        return html_str
    
    def generate_stat_boxes(self, stats):
        """Generate statistic boxes"""
        html_str = '<div class="card-grid">\n'
        for stat in stats:
            html_str += f"""
            <div class="stat-box">
                <div class="number">{self._escape(stat['value'])}</div>
                <div class="label">{self._escape(stat['label'])}</div>
            </div>
            """
        html_str += "</div>\n"
        return html_str
    
    def generate_bar_chart(self, data, title=None, max_value=None):
        """Generate a simple horizontal bar chart"""
        html_str = ""
        if title:
            html_str += f"<h3>{self._escape(title)}</h3>\n"
        
        if max_value is None:
            max_value = max(item['value'] for item in data) if data else 1
        
        for item in data:
            percentage = (item['value'] / max_value * 100) if max_value else 0
            html_str += f"""
            <div class="chart-bar">
                <div class="chart-bar-label">{self._escape(item['label'])}</div>
                <div class="chart-bar-bg">
                    <div class="chart-bar-fill" style="width: {percentage}%"></div>
                </div>
                <div class="chart-bar-value">{self._escape(str(item['value']))}</div>
            </div>
            """
        return html_str
    
    def generate_cards(self, items, template_func):
        """Generate card layout with custom template"""
        html_str = '<div class="card-grid">\n'
        for item in items:
            html_str += f'<div class="card">\n{template_func(item)}\n</div>\n'
        html_str += "</div>\n"
        return html_str
    
    def badge(self, text, style="info"):
        """Generate a badge"""
        return f'<span class="badge badge-{style}">{self._escape(text)}</span>'
    
    def generate_report(self, sections):
        """Generate complete report"""
        html_str = self._generate_header()
        html_str += f'<div class="report">\n'
        html_str += f'<h1>{self._escape(self.title)}</h1>\n'
        
        for section in sections:
            if section.get('title'):
                html_str += f'<h2>{self._escape(section["title"])}</h2>\n'
            html_str += section.get('content', '') + "\n"
        
        html_str += '</div>\n'
        html_str += self._generate_footer()
        return html_str


def demo_user_report():
    """Generate a sample user report"""
    generator = HTMLReportGenerator("User Analytics Report")
    
    # Sample data
    users = [
        {"name": "John Doe", "email": "john@example.com", "status": "Active", "orders": 42},
        {"name": "Jane Smith", "email": "jane@example.com", "status": "Active", "orders": 38},
        {"name": "Bob Wilson", "email": "bob@example.com", "status": "Inactive", "orders": 15},
        {"name": "Alice Brown", "email": "alice@example.com", "status": "Active", "orders": 67},
        {"name": "Charlie Davis", "email": "charlie@example.com", "status": "Pending", "orders": 8},
    ]
    
    # Statistics
    stats = [
        {"value": len(users), "label": "Total Users"},
        {"value": sum(u['orders'] for u in users), "label": "Total Orders"},
        {"value": len([u for u in users if u['status'] == 'Active']), "label": "Active Users"},
        {"value": f"${sum(u['orders'] for u in users) * 29.99:.2f}", "label": "Revenue"},
    ]
    
    # Bar chart data
    chart_data = [
        {"label": u["name"], "value": u["orders"]} for u in users
    ]
    
    # User card template
    def user_card(user):
        status_style = "success" if user['status'] == 'Active' else "warning" if user['status'] == 'Pending' else "danger"
        return f"""
        <h4>{generator._escape(user['name'])}</h4>
        <p>📧 {generator._escape(user['email'])}</p>
        <p>📦 Orders: {user['orders']}</p>
        <p>Status: {generator.badge(user['status'], status_style)}</p>
        """
    
    # Table data
    table_headers = ["Name", "Email", "Status", "Orders"]
    table_rows = [[u["name"], u["email"], u["status"], u["orders"]] for u in users]
    
    # Build report sections
    sections = [
        {"title": "Overview", "content": generator.generate_stat_boxes(stats)},
        {"title": "Orders by User", "content": generator.generate_bar_chart(chart_data)},
        {"title": "User Cards", "content": generator.generate_cards(users, user_card)},
        {"title": "User Table", "content": generator.generate_table(table_headers, table_rows)},
    ]
    
    report_html = generator.generate_report(sections)
    
    # Save report
    filename = "/tmp/user_report.html"
    with open(filename, "w") as f:
        f.write(report_html)
    
    print(f"\n✅ Report generated: {filename}")
    print(f"   Open in browser to view the report.")
    
    return report_html


def demo_sales_report():
    """Generate a sample sales report"""
    generator = HTMLReportGenerator("Monthly Sales Report")
    
    # Sample sales data
    sales = [
        {"product": "Widget Pro", "units": 150, "revenue": 4500, "category": "Electronics"},
        {"product": "Gadget Plus", "units": 89, "revenue": 2670, "category": "Electronics"},
        {"product": "Super Tool", "units": 234, "revenue": 3510, "category": "Tools"},
        {"product": "Smart Device", "units": 67, "revenue": 6700, "category": "Electronics"},
        {"product": "Power Pack", "units": 120, "revenue": 1800, "category": "Accessories"},
    ]
    
    # Stats
    total_units = sum(s['units'] for s in sales)
    total_revenue = sum(s['revenue'] for s in sales)
    
    stats = [
        {"value": f"${total_revenue:,}", "label": "Total Revenue"},
        {"value": f"{total_units:,}", "label": "Units Sold"},
        {"value": len(sales), "label": "Products"},
        {"value": f"${total_revenue/total_units:.2f}", "label": "Avg Price"},
    ]
    
    # Revenue chart
    chart_data = [
        {"label": s["product"][:15], "value": s["revenue"]} for s in sales
    ]
    
    # Table
    headers = ["Product", "Category", "Units Sold", "Revenue"]
    rows = [[s["product"], s["category"], s["units"], f"${s['revenue']:,}"] for s in sales]
    
    sections = [
        {"title": "Summary", "content": generator.generate_stat_boxes(stats)},
        {"title": "Revenue by Product", "content": generator.generate_bar_chart(chart_data)},
        {"title": "Sales Details", "content": generator.generate_table(headers, rows)},
    ]
    
    report_html = generator.generate_report(sections)
    
    filename = "/tmp/sales_report.html"
    with open(filename, "w") as f:
        f.write(report_html)
    
    print(f"\n✅ Sales report generated: {filename}")
    
    return report_html


def main():
    """Run demos"""
    print("\n🚀 HTML Report Generator Demo\n")
    
    print("1️⃣ Generating User Analytics Report...")
    demo_user_report()
    
    print("\n2️⃣ Generating Sales Report...")
    demo_sales_report()
    
    print("\n✅ All reports generated!")
    print("Open the HTML files in a browser to view them.")


if __name__ == "__main__":
    main()
