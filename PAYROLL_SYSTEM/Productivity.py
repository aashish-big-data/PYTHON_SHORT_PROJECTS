class ProductivitySystem:
    def track(self, employees, hours):
        print('Employee Productivity')
        print('==============================')
        for employee in employees:
            employee.work(hours)
        print('')
        
