"""
# Employee info
class Employee(object):
    def __init__(self, id, importance, subordinates):
        # It's the unique id of each node.
        # unique id of this employee
        self.id = id
        # the importance value of this employee
        self.importance = importance
        # the id of direct subordinates
        self.subordinates = subordinates
"""
class Solution(object):
    def getImportance(self, employees, id):
        """
        :type employees: Employee
        :type id: int
        :rtype: int
        """
        d = {employee.id:employee for employee in employees}
        # def dfs(id):
        #     return d[id].importance + sum([dfs(sub_id) for sub_id in d[id].subordinates])
        # return dfs(id)
        stack = [d[id]]
        res = 0
        while stack:
            employee = stack.pop()
            res+= employee.importance
            for sub in employee.subordinates:
                stack.append(d[sub])
        return res