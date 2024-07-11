# status-manager python library
## simple and useful status manager for bulk computations
Assume that you have multiple folders which each one have a complete and isolated computation task.
When you need to run them in sequence, may be it waste your time to count the current stage of each one. With this library you can easily handle the progress of each computation inside their own folders.    

# Usage
For example assume there are 4 folders inside the working directory, each one has a computation of calculating solar energy of a planet. Now you are going to start computation for them which are not finished from previous attempts. I mean something like this:
```python
for i in range(1, 5):
        task = f"task-{i}"
        os.system(f"{task}/run_calculations") # run calculations
```

By using `status-manager`, it will be very easy! See this example:

# Example

```python
from status_manager import CheckStatus, StatusType

s = CheckStatus() # init the status manager

for i in range(1, 5):
        task = f"task-{i}"
        status = s.check(task) # read status of this task
        if status != StatusType.finished:
            os.system(f"{task}/run_calculations") # run calculations
            status.write_status(task, StatusType.finished) # save as finished
```
