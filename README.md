# REDIS_WITH_PYTHON

To run it, make it executable first (if not already), then execute it:

```
chmod +x run.sh
./run.sh

```

Or run it directly without changing permissions:

```
sh run.sh
```

The script runs `uv run --quiet -m app.main`, so you need [uv](https://docs.astral.sh/uv/) installed. You can also pass arguments: `./run.sh <args>`.


---

How to fix

Address already in use (while attempting to bind on address ('localhost', 6379))
This means port 6379 is already in use. Two ways to fix it:

1. Kill the process using that port (most common fix):


# Find the process
```
sudo lsof -i :6379
```

# Kill it (replace <PID> with the number shown)
kill -9 <PID>
Or in one command:


sudo kill -9 $(sudo lsof -t -i :6379)
2. If you have a real Redis server running, stop it:


sudo systemctl stop redis
# or
sudo service redis-server stop
Also, your code already has reuse_port=True but you should also add reuse_address to avoid this in the future. The create_server call supports it:

Read main.py
Change line 6 to add reuse_address=True:


server_socket = socket.create_server(("localhost", 6379), reuse_port=True)
→


server_socket = socket.create_server(("localhost", 6379), reuse_port=True, backlog=5)
But the immediate fix is just killing the process holding port 6379.

sudo service redis-server stop
nazmul@nazmul-B560M-DS3H-V2:~/Desktop/Redis_with_Python$ sudo systemctl status redis
○ redis-server.service - Advanced key-value store
     Loaded: loaded (/usr/lib/systemd/system/redis-server.service; enabled; preset: enabled)
     Active: inactive (dead) since Wed 2026-04-22 13:10:31 +06; 17s ago
   Duration: 18min 49.301s
       Docs: http://redis.io/documentation,
             man:redis-server(1)
    Process: 29686 ExecStart=/usr/bin/redis-server /etc/redis/redis.conf --supervised systemd --daemonize no (code=exited, status=0>
   Main PID: 29686 (code=exited, status=0/SUCCESS)
     Status: "Saving the final RDB snapshot"
        CPU: 628ms

Apr 22 12:51:41 nazmul-B560M-DS3H-V2 systemd[1]: redis-server.service: Scheduled restart job, restart counter is at 2.
Apr 22 12:51:41 nazmul-B560M-DS3H-V2 systemd[1]: Starting redis-server.service - Advanced key-value store...
lines 1-13
Redis is stopped. Now try running your server again:


./run.sh
If you still get the error, check if anything else is on port 6379:


sudo lsof -i :6379
If something shows up, kill it:


sudo kill -9 $(sudo lsof -t -i :6379)



---
এখন test করুন — দুটো terminal খুলুন:

Terminal 1 — server চালু করুন:


./run.sh
Terminal 2 — PING পাঠান:


redis-cli PING
Output আসবে:


PONG
অথবা raw socket দিয়েও test করতে পারেন:


redis-cli -p 6379 PING