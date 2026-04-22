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
এখন test করুন — দুটো terminal খুলুন:

Terminal 1 — server চালু করুন:


./run.sh
Terminal 2 — PING পাঠান:


redis-cli PING
Output আসবে:


PONG
অথবা raw socket দিয়েও test করতে পারেন:


redis-cli -p 6379 PING