练习...

---

**目标**

* 精简执行流程，减少函数调用次数和中间对象数量。
* 按需装配，选择合适的组件作为驱动。


**功能**:

* 默认核心基于 gevent pywsgi，greenlet 协程并发。
* 使用 thread pool 完成异步调用，logic 无需改动。
* 将标记好的 logic 放到 action 目录，系统自动载入执行。
* 提供 debug 模式，支持异常现场调试，profile 输出。
* 如子进程意外终止，自动新建，确保服务进程数量。
* 支持用信号终止或新增工作子进程。

**使用**:

    $ pip install -r requirements.txt
    $ ./run.py
    # 如果想指定监听端口
    $ ./run.py -p 8000

**TODO**

* 动态调度器。
* 监控。
* 使用 Cython 编写/优化部分算法。
