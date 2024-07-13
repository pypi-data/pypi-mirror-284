#!/usr/bin/env python3

import argparse
import numpy as np
import pmpred as pm
import time


def main():
    parser = argparse.ArgumentParser(
        description="Using Precision Matrix, Snplists and Sumstats to give a joint effective size"
    )
    parser.add_argument("--pm", type=str, help="Precision Matrix Folder Path")
    parser.add_argument("--snp", type=str, help="Snplists Folder Path")
    parser.add_argument("-s", "--sumstats", type=str, help="Sumstats File")
    parser.add_argument("-o", "--out", type=str, help="Output File")
    parser.add_argument(
        "--burnin",
        type=int,
        default=50,
        help="The number of burn-in iterations used by the Gibbs sampler The default is 50.",
    )
    parser.add_argument(
        "--numiter",
        type=int,
        default=100,
        help="The number of iterations used by the Gibbs sampler. The default is 100.",
    )
    parser.add_argument(
        "--taylor",
        type=int,
        default=10,
        help="The number of approximation in taylor expansion. The default is 100.",
    )
    parser.add_argument(
        "--h2",
        type=float,
        default=np.random.rand(),
        help="The genome-wide heritability assumed by PMpred. The default is random",
    )
    parser.add_argument(
        "--p",
        type=float,
        default=np.random.rand(),
        help="The prior probability of non-sparse. The default is random",
    )
    parser.add_argument(
        "--njobs",
        type=int,
        default=-1,
        help="The jobs parallelized. The default is -1",
    )
    parser.add_argument(
        "--method",
        type=int,
        default=0,
        help="The method we use in PMpred, 0: PMpred-auto, 1: PMpred-grid, 2: normalize PM matrix. The default is auto",
    )
    parser.add_argument(
        "--unnormal",
        action="store_true",
        help="If select, then will not do normalization step for Precision Matrix",
    )
    parser.add_argument(
        "--rtol",
        type=float,
        default=1e-8,
        help="Thr precision of gmres algorithm to solve the linear equation. The default is 1e-8",
    )

    args = parser.parse_args()
    para = pm.generate.get_para()
    para["h2"] = args.h2
    para["p"] = args.p
    para["ldgm_burn_in"] = args.burnin
    para["ldgm_num_iter"] = args.numiter
    para["taylor_num"] = args.taylor
    para["n_jobs"] = args.njobs
    para["rtol"] = args.rtol
    if args.method == 0:
        if not args.pm:
            parser.error("You must specify a Precision Matrix Folder Path.")
        if not args.snp:
            parser.error("You must specify a Snplists Folder Path.")
        if not args.sumstats:
            parser.error("You must specify a Sumstats File.")
        start_time = time.time()
        sumstats = pm.Read.sumstats_read(args.sumstats)
        pm.Fliter.fliter_by_unique_sumstats(sumstats)
        PM = pm.Read.PM_read(args.pm)
        snplist = pm.Read.snplist_read(args.snp)
        pm.Fliter.filter_by_PM(PM, snplist)
        if not args.unnormal:
            pm.Fliter.normalize_PM_parallel(PM, para)
        sumstats_set = pm.Fliter.fliter_by_sumstats_parallel(
            PM, snplist, sumstats, para
        )
        pm.Check.check_same_rsid(snplist, sumstats_set)
        beta_ldgm, p, h2 = pm.PMpred.ldgm_gibbs_block_auto_parallel(
            PM, snplist, sumstats_set, para
        )
        end_time = time.time()
        pm.Write.sumstats_beta_write(
            sumstats_set, beta_ldgm, args.out, end_time - start_time, p, h2
        )
    elif args.method == 1:
        if not args.pm:
            parser.error("You must specify a Precision Matrix Folder Path.")
        if not args.snp:
            parser.error("You must specify a Snplists Folder Path.")
        if not args.sumstats:
            parser.error("You must specify a Sumstats File.")
        start_time = time.time()
        sumstats = pm.Read.sumstats_read(args.sumstats)
        pm.Fliter.fliter_by_unique_sumstats(sumstats)
        PM = pm.Read.PM_read(args.pm)
        snplist = pm.Read.snplist_read(args.snp)
        pm.Fliter.filter_by_PM(PM, snplist)
        if not args.unnormal:
            pm.Fliter.normalize_PM_parallel(PM, para)
        sumstats_set = pm.Fliter.fliter_by_sumstats_parallel(
            PM, snplist, sumstats, para
        )
        pm.Check.check_same_rsid(snplist, sumstats_set)
        beta_ldgm = pm.PMpred.ldgm_gibbs_block_grid_parallel(
            PM, snplist, sumstats_set, para
        )
        end_time = time.time()
        pm.Write.sumstats_beta_write(
            sumstats_set,
            beta_ldgm,
            args.out,
            end_time - start_time,
            para["p"],
            para["h2"],
        )
    elif args.method == 2:
        if not args.pm:
            parser.error("You must specify a Precision Matrix Folder Path.")
        PM = pm.Read.PM_read(args.pm)
        pm.Fliter.normalize_PM_parallel(PM, para)
        pm.Write.PM_write(PM, args.out)
    else:
        parser.error(
            "You must choose a method in {0: PMpred-auto, 1: PMpred-grid, 2: normalize PM matrix}"
        )


if __name__ == "__main__":
    main()
