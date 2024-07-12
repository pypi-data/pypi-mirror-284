#!/usr/bin/env Rscript
#library(phytools)
library(castor)
library(ape)

# disable warnings
options(warn = -1)

# example command string to simulate for "out.1" through "out.10"
# cd ~/projects/phyddle/scripts
# Rscript sim_bisse.R ./simulate out 1 10

# arguments
args        = commandArgs(trailingOnly = TRUE)
out_path    = args[1]
out_prefix  = args[2]
start_idx   = as.numeric(args[3])
batch_size  = as.numeric(args[4])
rep_idx     = start_idx:(start_idx+batch_size-1)
num_rep     = length(rep_idx)
get_mle     = FALSE

# filesystem
tmp_fn = paste0(out_path, "/", out_prefix, ".", rep_idx)   # sim path prefix
phy_fn = paste0(tmp_fn, ".tre")               # newick file
dat_fn = paste0(tmp_fn, ".dat.csv")           # csv of data
lbl_fn = paste0(tmp_fn, ".labels.csv")        # csv of labels (e.g. params)

# dataset setup
num_states = 2
symm_Q_mtx = TRUE
tree_width = 500
label_names = c( "log_birth_1",
                 "log_birth_2",
                 "log_death",
                 "log_state_rate",
                 "log_sample_frac")

# simulate each replicate
for (i in 1:num_rep) {

    # set RNG seed
    set.seed(rep_idx[i])

    # rejection sample
    num_taxa = 0
    while (num_taxa < 10) {
        
        # simulation conditions
        max_taxa = runif(1, 10, 5000)
        max_time = runif(1, 1, 100)
        sample_frac = 0.9999
        if (max_taxa > tree_width) {
            sample_frac = tree_width / max_taxa
        }

        # simulate parameters
        start_state = sample(1:2, size=1)
        state_rate = runif(n=1, 0.0, 1.0)
        Q = matrix(state_rate,
                   ncol=num_states, nrow=num_states)
        diag(Q) = 0
        diag(Q) = -rowSums(Q)
        birth = runif(n=num_states, 0.0, 1.0)
        death = runif(n=1, 0.0, 1.0)
        death = rep(death, num_states)
        parameters = list(
            birth_rates=birth,
            death_rates=death,
            transition_matrix_A=Q
        )

        # simulate tree/data
        res_sim = simulate_dsse(
                Nstates=num_states,
                parameters=parameters,
                start_state=start_state,
                sampling_fractions=sample_frac,
                max_extant_tips=max_taxa,
                max_time=max_time,
                include_labels=T,
                no_full_extinction=T)

        # check if tree is valid
        num_taxa = length(res_sim$tree$tip.label)
    }
   
    # save tree
    tree_sim = res_sim$tree
    write.tree(tree_sim, file=phy_fn[i])

    # save data
    state_sim = res_sim$tip_states - 1
    df_state = data.frame(taxa=tree_sim$tip.label, data=state_sim)
    write.csv(df_state, file=dat_fn[i], row.names=F, quote=F)

    # save learned labels (e.g. estimated data-generating parameters)
    log_sample_frac = log(sample_frac, base=10)
    log_state_rate = log(state_rate, base=10)
    log_birth = log(birth, base=10)
    log_death = log(death[1], base=10)
    label_sim = c( log_birth[1], log_birth[2], log_death, log_state_rate, log_sample_frac)
    names(label_sim) = label_names
    df_label = data.frame(t(label_sim))
    write.csv(df_label, file=lbl_fn[i], row.names=F, quote=F)

}


# done!
quit()
