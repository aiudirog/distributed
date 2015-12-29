import logging


logger = logging.getLogger(__name__)


class SchedulerPlugin(object):
    """ Interface to extend the Scheduler

    The scheduler operates by triggering and responding to events like
    ``task_finished``, ``update_graph``, ``task_erred``, etc..

    A plugin enables custom code to run at each of those same events.  The
    scheduler will run the analagous methods on this class when each event is
    triggered.  This runs user code within the scheduler thread that can
    perform arbitrary operations in synchrony with the scheduler itself.

    Plugins are often used for diagnostics and measurement, but have full
    access to the scheduler and could in principle affect core scheduling.

    To implement a plugin implement some of the methods of this class and add
    the plugin to the scheduler with ``Scheduler.add_plugin(myplugin)``.

    Examples
    --------
    >>> class Counter(SchedulerPlugin):
    ...     def __init__(self):
    ...         self.counter = 0
    ...
    ...     def task_finished(self, scheduler, key, worker, nbytes):
    ...         self.counter += 1
    ...
    ...     def restart(self, scheduler):
    ...         self.counter = 0

    >>> c = Counter()
    >>> scheduler.add_plugin(c)  # doctest: +SKIP
    """
    def task_finished(self, scheduler, key, worker, nbytes):
        """ Run when a task is reported complete """
        pass

    def update_graph(self, scheduler, dsk, keys, restrictions):
        """ Run when a new graph / tasks enter the scheduler """
        pass

    def task_erred(self, scheduler, key, worker, exception):
        """ Run when a task is reported failed """
        pass

    def restart(self, scheduler):
        """ Run when the scheduler restarts itself """
        pass

