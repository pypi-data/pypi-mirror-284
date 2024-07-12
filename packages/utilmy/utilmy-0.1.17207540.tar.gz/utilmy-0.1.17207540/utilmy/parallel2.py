__author__ = "Mulya Agung"
__email__ = "hey.mulya@gmail.com"

from utilmy.utilmy_base import log
import math
import time


def dummy_cpu_func(list_vars, const=1, const2=1):
    start_time = time.time()
    print(f'Var: {list_vars}')
    print('Fixed Const: ', const, const2)
    while time.time() - start_time < 50 / 100.0:
        v = math.sqrt(2 * sum([i[0] for i in list_vars]))
    return f"{v} {str(list_vars[0])} "


def batched_run(myfunc, input_batch: list):
    return [[] if not i else myfunc(i) for i in input_batch]


def mp_batched_run(fun_async, input_list: list, n_pool=5, start_delay=0.1, verbose=False, input_fixed: dict = None,
                   npool=None, **kw):
    """  Run input_list in parallel with multiprocessing and batching.
    Doc::
        def test_func(list_vars, const=1, const2=1):
            print(f'Var: {list_vars[0]}')
            print('Fixed Const: ', const)
            return f"{const*const2} {str(list_vars[0])}"

        input_arg   = [ ( [1,2, "Hello"], [2,4, "World"], [3,4, "Thread3"], [4,5, "Thread4"], [5,2, "Thread5"], ),    ]
        input_fixed = {'const': 50, 'const2': i}

        from utilmy import parallel as par
        res = par.mp_batched_run(test_func, input_arg, n_pool=3, input_fixed=input_fixed)
        print(res)

    """
    import functools
    import multiprocessing

    if not input_list:
        results = []
    else:
        if input_fixed is not None:
            fun_async = functools.partial(fun_async, **input_fixed)

        n_pool = npool if isinstance(npool, int) else n_pool  # alias

        # Distribute inputs to pooled processes
        num_inputs = len(input_list)
        num_processes = min(n_pool, num_inputs)
        input_chunk_size, rem = divmod(num_inputs, num_processes)

        with multiprocessing.Pool(processes=num_processes) as pool:
            refs = []
            for p in range(num_processes):
                chunk_start, chunk_end = p * input_chunk_size, (p + 1) * input_chunk_size
                if rem > 0 and p == num_processes - 1:
                    chunk_end += rem

                refs.append(pool.apply_async(batched_run, args=(fun_async, input_list[chunk_start:chunk_end])))

                if verbose:
                    log(p, input_list[chunk_start:chunk_end])

            # Wait for results
            results = [r for b in [ref.get() for ref in refs] for r in b]
            log('n_processed', len(results))

    return results


if __name__ == '__main__':
    input_args = [[[i, j, "{}-{}".format(i, j)] for j in range(10)] for i in range(10)]
    input_fixed = {'const': 50, 'const2': 10}
    mp_pool = 3

    res = mp_batched_run(dummy_cpu_func, input_args, n_pool=mp_pool, input_fixed=input_fixed)
    print(res)
