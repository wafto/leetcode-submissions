class Task:
    def __init__(self, id: int, priority: int, user: int):
        self.id = id
        self.priority = priority
        self.user = user
        self.stale = False

    def __lt__(self, other) -> bool:
        if self.priority == other.priority:
            return self.id > other.id
        return self.priority > other.priority

class TaskManager:

    def __init__(self, tasks: List[List[int]]):
        self.tasks = [Task(t, p, u) for u, t, p in tasks]
        self.mapping = {task.id: task for task in self.tasks}
        heapify(self.tasks)

    def add(self, userId: int, taskId: int, priority: int) -> None:
        task = Task(taskId, priority, userId)
        heappush(self.tasks, task)
        self.mapping[task.id] = task

    def edit(self, taskId: int, newPriority: int) -> None:
        current = self.mapping[taskId]
        task = Task(current.id, newPriority, current.user)
        current.stale = True
        self.mapping[taskId] = task
        heappush(self.tasks, task)

    def rmv(self, taskId: int) -> None:
        current = self.mapping[taskId]
        current.stale = True

    def execTop(self) -> int:
        while self.tasks:
            task = heappop(self.tasks)
            if not task.stale:
                return task.user

        return -1


# Your TaskManager object will be instantiated and called as such:
# obj = TaskManager(tasks)
# obj.add(userId,taskId,priority)
# obj.edit(taskId,newPriority)
# obj.rmv(taskId)
# param_4 = obj.execTop()