class ScopeManager:
    def __init__(self):
        self.scopes = [{}]  # Start with the global scope
        self.scope_depth = 0
        self.block_number = 0

    # ID: Value(name[ID, value or reference], type, length)
    # varA: Value(varA, int, 0)
    # varA: Value(%3, int, 0)
    # varA: Value(15, int, 0)

    def enter_scope(self):
        self.scopes.append({})  # Start a new local scope
        self.scope_depth += 1

    def exit_scope(self):
        self.scopes.pop()  # Exit the current scope
        self.scope_depth -= 1
        self.block_number += 1

    def declare_variable(self, ID, value):
        if ID in self.current_scope():
            raise Exception("Variable redeclaration error")
        self.current_scope()[ID] = value
        scoped = self.create_scoped_id(ID)
        self.current_scope()["id" + ID] = scoped
        return scoped

    def assign_value_to_variable(self, ID, new_value):
        # Update the variable in the most local scope it is found
        for scope in reversed(self.scopes):
            if ID in scope:
                scope[ID] = new_value
                return self.get_scoped_id(ID)
        raise KeyError(f"Variable {ID} not found in any scope.")

    def lookup_variable(self, ID):
        # Look up from the current scope to the global scope
        for scope in reversed(self.scopes):
            if ID in scope:
                return scope[ID]
        exception = f"Variable: {ID} not declared"
        raise Exception(exception)

    def get_scoped_id(self, ID):
        scoped_idx = "id" + ID
        for depth, scope in enumerate(reversed(self.scopes)):
            if scoped_idx in scope:
                return scope[scoped_idx]
        raise Exception("Variable not declared")

    def create_scoped_id(self, ID):
        for depth, scope in enumerate(reversed(self.scopes)):
            if ID in scope:
                if depth == len(self.scopes) - 1:
                    return f"@{ID}"
                else:
                    nesting = len(self.scopes) - 1 - depth
                    return f"%{ID}.{self.block_number}.{nesting}"
        raise Exception("Variable not declared")

    def current_scope(self):
        return self.scopes[-1]

    def is_global_variable(self, ID):
        return ID in self.scopes[0] and self.is_global()

    def is_global(self):
        return len(self.scopes) == 1


scope_manager = ScopeManager()
