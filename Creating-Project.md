### Remove folders and files from project

Open the `.sublime-project` file

Insert `folder_exclude_patterns` to ignore folders and `file_exclude_patterns` to ignore files.

```
{
   "folders":
   [
      {
         "path": "/home/jack/workspace/myproject",
         "folder_exclude_patterns": ["*", "*"],
         "file_exclude_patterns": ["*", "*"]
      }
   ]
}
```