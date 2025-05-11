# #60DaysofDevOps Challenge - Day 1

## Challenge 1: List all files (including hidden ones) in your home directory and sort them by modification time.
```bash
ls -alht ~
```
- `-a` - Show hidden files
- `-l` - Use long listing format
- `-h` - Display size in human readable format (KB, MB)
- `-t` - Sort by modification time (newest first)

## Challenge 2: Create a directory named devops_challenge_day_1, navigate into it, and create an empty file named day1.txt.
```bash
mkdir devops_challenge_day_1
cd devops_challenge_day_1
touch day1.txt
```

## Challenge 3: Find the total disk usage of the /var/log directory in human-readable format.
```bash
du -sh /var/log
```
- `-s` - Summarize the size instead of listing individual files
- `-h` - Human-readable output format

## Challenge 4: Create a new user called devops_user and add them to the sudo group.
```bash
sudo useradd -aG sudo devops_user
```

To verify the user was created with proper group membership:
```bash
id devops_user
```

To set a password for the new user:
```bash
sudo passwd devops_user
```

## Challenge 5: Create a group called devops_team and add devops_user to that group.
```bash
sudo groupadd devops_team
sudo usermod -aG devops_team devops_user
```

To verify group membership:
```bash
id devops_user
```

## Challenge 6: Change the permissions of day1.txt to allow only the owner to read and write, but no permissions for others.
```bash
chmod 600 day1.txt
```
- Permission value breakdown: read (4) + write (2) + execute (1)
- `600` means read (4) + write (2) = 6 for owner, and 0 (no permissions) for group and others

## Challenge 7: Find all files in /etc that were modified in the last 7 days.
```bash
find /etc -type f -mtime -7
```
- `-type f` - Look for files only
- `-mtime -7` - Find files modified in the last 7 days

## Challenge 8: Write a one-liner command to find the most frequently used command in your shell history.
```bash
history | awk '{CMD[$2]++;} END {for (a in CMD) print CMD[a], a;}' | sort -nr | head -1
```

This command works by:
1. `history` - Shows your command history
2. `awk '{CMD[$2]++;} END {for (a in CMD) print CMD[a], a;}'` - Counts occurrences of each command
3. `sort -nr` - Sorts numerically in reverse order (highest count first)
4. `head -1` - Shows only the first result (most frequently used command)