library(reshape2)
library(ggplot2)
library(cowplot)

phyddle_mtx = read.csv("phyddle.conf_mtx.csv", head=T)
pulsr_mtx = read.csv("pulsr.conf_mtx.csv", head=T)
comp_mtx = read.csv("compare.conf_mtx.csv", head=T)

#rownames(pulsr_mtx)=rownames(phyddle_mtx)=c("BM","OU","EB","Lévy")
for (i in 1:ncol(phyddle_mtx)) {
    phyddle_mtx[,i] = phyddle_mtx[,i]# / sum(phyddle_mtx[,i])
    pulsr_mtx[,i] = pulsr_mtx[,i] #/ sum(pulsr_mtx[,i])
    comp_mtx[,i] = comp_mtx[,i] #/ sum(comp_mtx[,i])
}

mdl_names = c("BM", "OU", "EB", "Lévy")

phyddle_df = c()
pulsr_df = c()
comp_df = c()
for (i in 1:length(phyddle_mtx)) {
    for (j in 1:length(phyddle_mtx)) {
        phyddle_df = rbind(phyddle_df, c(mdl_names[i], mdl_names[j], phyddle_mtx[i,j]))
        pulsr_df = rbind(pulsr_df, c(mdl_names[i], mdl_names[j], pulsr_mtx[i,j]))
        comp_df = rbind(comp_df, c(mdl_names[i], mdl_names[j], comp_mtx[i,j]))
    }
}
phyddle_df = data.frame(phyddle_df)
pulsr_df = data.frame(pulsr_df)
comp_df = data.frame(comp_df)


max_val = max( 
    c(max(as.numeric(phyddle_df$X3)),
      max(as.numeric(pulsr_df$X3)),
      max(as.numeric(comp_df$X3)))
)
#title = c("CNN", "MLE + AIC", "CNN)
col = c("blue","red", "gold")
df_list = list(phyddle=phyddle_df, pulsr=pulsr_df, comp=comp_df)
p_list = list()
for (i in 1:length(df_list)) {
    df = df_list[[i]]
    colnames(df) = c("Est","True","Freq")
    df$Freq = as.numeric(df$Freq)
    df$Est = factor(df$Est, ordered=T, levels=mdl_names)
    df$True = factor(df$True, ordered=T, levels=mdl_names)
    
    p = ggplot(df, aes(y=Est,x=True,fill=Freq), colour = "white")
    p = p + geom_tile()
    #p = p + geom_text(aes(label=sprintf("%0.2f",Freq)))
    p = p + geom_text(aes(label=Freq))
    #p = p + scale_fill_gradient2(low = "white", high = col[i], limits=c(0,1))
    p = p + scale_fill_gradient2(low = "white", high = col[i], limits=c(0,max_val))
    p = p + scale_y_discrete(limits = rev)
    p = p + guides( fill="none" )
    p = p + theme(panel.background = element_blank())
    p = p + theme(panel.border=element_rect(fill = NA, colour='black',size=0.5))
    p = p + theme(plot.margin = unit(c(1,0.5,0.5,0.5), "cm"))
    if (i == 1) {
        p = p + xlab("True") + ylab("CNN")
    } else if (i == 2) {
        p = p + xlab("True") + ylab("AIC")
    } else if (i == 3) {
        p = p + xlab("AIC") + ylab("CNN")
    }
    p_list[[i]] = p
    
}

pg = plot_grid( plotlist=p_list, align="hv", nrow=1, labels=c("A","B","C"))
plot_fn = paste0("fig_cont_trait_test.pdf")
pdf(plot_fn, height=3, width=9)
print(pg)
dev.off()

