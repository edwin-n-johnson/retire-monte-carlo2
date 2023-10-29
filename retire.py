import click

@click.command()
@click.argument('balances', type=click.Path(exists=True))
#@click.option('--gui/--no-gui', default=False, help='Launch gui')
@click.option('--debug', '-d', type=click.IntRange(0, 2, clamp=True), default=0)
@click.option('-s', '--seed', default=0, help='Random number seed')
def cli(balances, debug, seed):
    level = {0: logging.WARNING, 1: logging.INFO, 2: logging.DEBUG}[debug]
    logging.basicConfig(filename='logs/debug.log', filemode='w',
                        format='%(levelname)s %(filename)s %(message)s',
                        level=level,
                        datefmt='%H:%M:%S')
    logging.info("Loading account data from: {}".format(balances))

    if seed:
        np.random.seed(int(seed))

    gui = False
    # the main Tkinter window
    window = tk.Tk()
    # setting the title
    window.title('Monte Carlo Retirement Simulation')
    # dimensions of the main window
    window.geometry("800x800")

    # logging.debug("Created options: \n{}".format(str(options)))

    if gui:
        run_gui(window, balances, withdraws, None)
    else:
        run_simulator_and_plot_results(window, balances, withdraws, None)

    # run the gui
    window.mainloop()
