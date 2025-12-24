import json

class TestReportBuilder:
    def __init__(self, tests_file, values_file, report_file):
        self.tests_file = tests_file
        self.values_file = values_file
        self.report_file = report_file
        self.values_dict = {}
    
    def load_data(self):
        with open(self.tests_file, 'r', encoding='utf-8') as f:
            self.tests_data = json.load(f)
        
        with open(self.values_file, 'r', encoding='utf-8') as f:
            values_data = json.load(f)
        

        for item in values_data['values']:
            self.values_dict[item['id']] = item['value']
    
    def update_test_value(self, test_node):
        if 'id' in test_node and test_node['id'] in self.values_dict:
            test_node['value'] = self.values_dict[test_node['id']]
        
        if 'values' in test_node:
            for child in test_node['values']:
                self.update_test_value(child)
    
    def build_report(self):
        report_data = json.loads(json.dumps(self.tests_data))
        
        if 'tests' in report_data:
            for test in report_data['tests']:
                self.update_test_value(test)
        
        return report_data
    
    def save_report(self, report_data):
        with open(self.report_file, 'w', encoding='utf-8') as f:
            json.dump(report_data, f, indent=2, ensure_ascii=False)
    
    def run(self):
        self.load_data()
        report = self.build_report()
        self.save_report(report)
        print(f"Отчет успешно сохранен в {self.report_file}")

if __name__ == "__main__":
    builder = TestReportBuilder('tests.json', 'values.json', 'report.json')
    builder.run()