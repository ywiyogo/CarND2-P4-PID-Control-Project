import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import click

@click.command()
@click.argument("output")


def main(output):
    print("Output file: ", output)
    df = pd.read_table(output, sep='\t')
    print(df.head(n=5))

    fig = plt.figure(figsize=(16, 8))

    fig.suptitle('Using Break vs No Break', fontsize=18, fontweight='bold')
    ax1 = fig.add_subplot(121)
    fig.subplots_adjust(top=0.85)
    ax1.set_title('CTE Graph', fontsize=18, fontweight='bold')
    ax1.set_xlabel('time')
    ax1.set_ylabel('CTE')
    # ax1.plot(df['CTE(0.1)'])
    # ax1.plot(df['CTE(0.05)'])
    # ax1.plot(df['CTE(0.02)'])
    # ax1.plot(df['CTE(P:0.05;D:1)'])
    # ax1.plot(df['CTE(P:0.05;D:2)'])
    # ax1.plot(df['CTE(P:0.05;D:0.5)'])
    ax1.plot(df['CTE-0.12-0.009-1.8'])
    ax1.plot(df['CTE-0.12-0.009-1.8-NoBreak'])
    # ax1.plot(df['CTE-0.12-0.003-2.1'])
    # ax1.plot(df['CTE-0.12-0.002-2.1'])
    # ax1.plot(df['CTE(0.05,0.001, 0.7)'])
    # ax1.plot(df['CTE(0.05,0.0001, 1)'])
    # ax1.plot(df['CTE(0.1,0.0001, 1)'])
    #ax1.plot(df['CTE6'])
    #ax1.plot(df['Steer_value(0.05,0.001,0.5)'])
    # ax1.scatter(df["px_ground_truth"], df["py_ground_truth"],alpha=0.4, label = "ground truth")
    # ax1.scatter(df["px_state"], df["py_state"],alpha=0.7, marker='x', label = "UKF")
    ax1.legend(loc='upper left')
    ax1.grid(linestyle=":")

    ax2 = fig.add_subplot(122)
    ax2.set_title('Steer Value', fontsize=18, fontweight='bold')
    ax2.set_xlabel('time')
    ax2.set_ylabel('steer value')
    # ax2.plot(df['Steer_value(P:0.05;D:1)'])
    # ax2.plot(df['Steer_value(P:0.05;D:2)'])
    # ax2.plot(df['Steer_value(P:0.05;D:0.5)'])
    ax2.plot(df['SteerValue-0.12-0.009-1.8'])
    ax2.plot(df['SteerValue-0.12-0.009-1.8-NoBreak'])
    # ax2.plot(df['SteerValue-0.12-0.003-2.1'])
    # ax2.plot(df['SteerValue-0.12-0.002-2.1'])
    # ax2.plot(df['Steer_value(0.05,0.001, 0.7)'])
    # ax2.plot(df['Steer_value(0.05,0.0001, 1)'])
    # ax2.plot(df['Steer_value(0.1,0.0001, 1)'])
    #ax2.plot(df['Steer_value(0.1,0.0001, 1)'])
    ax2.legend(loc='upper left')
    ax2.grid(linestyle=":")

    fig.tight_layout()
    plt.savefig('experiments.png')

    plt.show()

if __name__ == '__main__':
    main()