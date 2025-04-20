class Task:
    """
    Class representing a task with a name and priority.
    
    The task priority determines the order of execution in the task management system.
    Tasks with high priority should be executed before tasks with low priority.
    """
    
    def __init__(self, name: str, priority: int):
        """
        Initializes a task with the specified name and priority.
        
        Args:
            name: Task name
            priority: Task priority (integer)
        """
        self.__name = name
        self.__priority = priority
    
    @property
    def priority(self) -> int:
        """
        Returns the task priority.
        
        Returns:
            int: Task priority
        """
        return self.__priority
    
    @property
    def name(self) -> str:
        """
        Returns the task name.
        
        Returns:
            str: Task name
        """
        return self.__name
    
    def __repr__(self) -> str:
        """
        Returns the string representation of the task.
        
        Returns:
            str: String representation in the format "Task(name, priority)"
        """
        return f"Task({self.__name}, {self.__priority})"


class TaskMess:
    """
    Class for analyzing problematic sections in a task list
    where priorities violate logical order.
    """
    
    @staticmethod
    def get_pair_of_tasks(tasks: list[Task]) -> tuple[int, int] | None:
        """
        Finds the minimum subarray of tasks that needs to be reordered
        to make the entire task list sorted either in ascending
        or descending order of priorities.
        
        Args:
            tasks: List of tasks to analyze
            
        Returns:
            tuple[int, int] | None: Pair of indices (start, end) of the problematic subarray,
                                   or None if the list is already sorted or impossible
                                   to fix by reordering a single subarray
        
        Examples:
            >>> tasks = [Task("A", 1), Task("B", 2), Task("C", 4), Task("D", 3), Task("E", 5)]
            >>> TaskMess.get_pair_of_tasks(tasks)
            (2, 3)
            
            >>> tasks = [Task("A", 5), Task("B", 4), Task("C", 2), Task("D", 3), Task("E", 1)]
            >>> TaskMess.get_pair_of_tasks(tasks)
            (2, 3)
            
            >>> tasks = [Task("A", 1), Task("B", 2), Task("C", 3), Task("D", 4), Task("E", 5)]
            >>> TaskMess.get_pair_of_tasks(tasks)
            None
        """
        pass