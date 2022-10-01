#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: Manisha Sirsat
@department: Data Management and Risk Analysis
@organization: InnovPlantProtect, Elvas, Portugal
@website: https://iplantprotect.pt/

"""

import os
os. chdir("/home/DataHub/WheatGP")

from library import *

# plotting heatmap for correlation train results on the loc1
df_heatmap = pd.read_csv('Analysis/Heatmap/resultDatasets/ResultTrainCorrModelLoc1.csv', header = 0, sep = ",")
df_heatmap=df_heatmap.set_index('Model')
sns.set(font_scale=1.2)
with sns.axes_style("darkgrid"):
    f, ax = plt.subplots(figsize=(9, 6))
    ax = sns.heatmap(df_heatmap, annot=True, vmin=0.10, vmax=0.75, linewidths=.01, cmap='viridis', annot_kws={"size": 14, "va": "center_baseline", "color": "white"})
    ax.set_facecolor('PowderBlue')
plt.setp(ax.get_xticklabels(), rotation=30, ha="right", rotation_mode="anchor")
plt.savefig('Analysis/Heatmap/Plots/Plot_TrainCorrModelLoc1.png')


# plotting heatmap for correlation train results on the loc2
df_heatmap = pd.read_csv('Analysis/Heatmap/resultDatasets/ResultTrainCorrModelLoc2.csv', header = 0, sep = ",")
df_heatmap=df_heatmap.set_index('Model')
sns.set(font_scale=1.2)
with sns.axes_style("darkgrid"):
    f, ax = plt.subplots(figsize=(9, 6))
    ax = sns.heatmap(df_heatmap, annot=True, vmin=0.10, vmax=0.75, linewidths=.01, cmap='viridis', annot_kws={"size": 14, "va": "center_baseline", "color": "white"})
    ax.set_facecolor('PowderBlue')
plt.setp(ax.get_xticklabels(), rotation=30, ha="right", rotation_mode="anchor")
plt.savefig('Analysis/Heatmap/Plots/Plot_TrainCorrModelLoc2.png')


# plotting heatmap for correlation train results on the loc3
df_heatmap = pd.read_csv('Analysis/Heatmap/resultDatasets/ResultTrainCorrModelLoc3.csv', header = 0, sep = ",")
df_heatmap=df_heatmap.set_index('Model')
sns.set(font_scale=1.2)
with sns.axes_style("darkgrid"):
    f, ax = plt.subplots(figsize=(9, 6))
    ax = sns.heatmap(df_heatmap, annot=True, vmin=0.10, vmax=0.75, linewidths=.01, cmap='viridis', annot_kws={"size": 14, "va": "center_baseline", "color": "white"})
    ax.set_facecolor('PowderBlue')
plt.setp(ax.get_xticklabels(), rotation=30, ha="right", rotation_mode="anchor")
plt.savefig('/Analysis/Heatmap/Plots/Plot_TrainCorrModelLoc3.png')


# plotting heatmap for correlation test results on the loc1
df_heatmap = pd.read_csv('Analysis/Heatmap/resultDatasets/ResultTestCorrModelLoc1.csv', header = 0, sep = ",")
df_heatmap=df_heatmap.set_index('Model')
sns.set(font_scale=1.2)
with sns.axes_style("darkgrid"):
    f, ax = plt.subplots(figsize=(9, 6))
    ax = sns.heatmap(df_heatmap, annot=True, vmin=0.10, vmax=0.75, linewidths=.01, cmap='viridis', annot_kws={"size": 14, "va": "center_baseline", "color": "white"})
    ax.set_facecolor('PowderBlue')
plt.setp(ax.get_xticklabels(), rotation=30, ha="right", rotation_mode="anchor")
plt.savefig('/Analysis/Heatmap/Plots/Plot_TestCorrModelLoc1.png')


# plotting heatmap for correlation test results on the loc2
df_heatmap = pd.read_csv('Analysis/Heatmap/resultDatasets/ResultTestCorrModelLoc2.csv', header = 0, sep = ",")
df_heatmap=df_heatmap.set_index('Model')
sns.set(font_scale=1.2)
with sns.axes_style("darkgrid"):
    f, ax = plt.subplots(figsize=(9, 6))
    ax = sns.heatmap(df_heatmap, annot=True, vmin=0.10, vmax=0.75, linewidths=.01, cmap='viridis', annot_kws={"size": 14, "va": "center_baseline", "color": "white"})
    ax.set_facecolor('PowderBlue')
plt.setp(ax.get_xticklabels(), rotation=30, ha="right", rotation_mode="anchor")
plt.savefig('/Analysis/Heatmap/Plots/Plot_TestCorrModelLoc2.png')


# plotting heatmap for correlation test results on the loc3
df_heatmap = pd.read_csv('Analysis/Heatmap/resultDatasets/ResultTestCorrModelLoc3.csv', header = 0, sep = ",")
df_heatmap=df_heatmap.set_index('Model')
sns.set(font_scale=1.2)
with sns.axes_style("darkgrid"):
    f, ax = plt.subplots(figsize=(9, 6))
    ax = sns.heatmap(df_heatmap, annot=True, vmin=0.10, vmax=0.75, linewidths=.01, cmap='viridis', annot_kws={"size": 14, "va": "center_baseline", "color": "white"})
    ax.set_facecolor('PowderBlue')
plt.setp(ax.get_xticklabels(), rotation=30, ha="right", rotation_mode="anchor")
plt.savefig('Analysis/Heatmap/Plots/Plot_TestCorrModelLoc3.png')


#Modelwise: plotting boxplot of train and test results of the loc1, loc2 and loc3 datasets
# plotting boxplot for correlation train results on the loc1
df_boxplotModel = pd.read_csv('Analysis/BoxPlotModel/resultDatasets/ResultTestCorrModelLoc1_boxplot.csv', header = 0, sep = ",")
df_boxplotModel['Corr']=np.round(df_boxplotModel['Corr'], 2) 
sns.set_theme(style="whitegrid");
#sns.set(font_scale=1.2)
f, ax = plt.subplots(figsize=(9, 6))    
ax = sns.boxplot(x='Model', y='Corr', data=df_boxplotModel, palette="Set1", showfliers=False)
#ax.set_facecolor('white')
ax.set_xticklabels(ax.get_xticklabels(),rotation=30)
ax.set_ylim([0.10,0.75])# add stripplot
ax = sns.stripplot(x='Model', y='Corr', data=df_boxplotModel, color="orange", jitter=0.25, size=5.0)
plt.show()
plt.savefig('Analysis/BoxPlotModel/Plots/ResultTestCorrModelLoc1_boxplot.png')

# plotting boxplot for correlation train results on the loc2
df_boxplotModel = pd.read_csv('Analysis/BoxPlotModel/resultDatasets/ResultTestCorrModelLoc2_boxplot.csv', header = 0, sep = ",")
df_boxplotModel['Corr']=np.round(df_boxplotModel['Corr'], 2) 
sns.set_theme(style="whitegrid");
#sns.set(font_scale=1.2)
f, ax = plt.subplots(figsize=(9, 6))    
ax = sns.boxplot(x='Model', y='Corr', data=df_boxplotModel, palette="Set1", showfliers=False)
#ax.set_facecolor('white')
ax.set_xticklabels(ax.get_xticklabels(),rotation=30)
ax.set_ylim([0.10,0.75])# add stripplot
ax = sns.stripplot(x='Model', y='Corr', data=df_boxplotModel, color="orange", jitter=0.25, size=5.0)
plt.show()
plt.savefig('Analysis/BoxPlotModel/Plots/ResultTestCorrModelLoc2_boxplot.png')

# plotting boxplot for correlation train results on the loc3
df_boxplotModel = pd.read_csv('Analysis/BoxPlotModel/resultDatasets/ResultTestCorrModelLoc3_boxplot.csv', header = 0, sep = ",")
df_boxplotModel['Corr']=np.round(df_boxplotModel['Corr'], 2) 
sns.set_theme(style="whitegrid");
#sns.set(font_scale=1.2)
f, ax = plt.subplots(figsize=(9, 6))    
ax = sns.boxplot(x='Model', y='Corr', data=df_boxplotModel, palette="Set1", showfliers=False)
#ax.set_facecolor('white')
ax.set_xticklabels(ax.get_xticklabels(),rotation=30)
ax.set_ylim([0.10,0.75])# add stripplot
ax = sns.stripplot(x='Model', y='Corr', data=df_boxplotModel, color="orange", jitter=0.25, size=5.0)
plt.show()
plt.savefig('/Analysis/BoxPlotModel/Plots/ResultTestCorrModelLoc3_boxplot.png')


# plotting boxplot for correlation test results on the loc1
df_boxplotModel = pd.read_csv('Analysis/BoxPlotModel/resultDatasets/ResultTrainCorrModelLoc1_boxplot.csv', header = 0, sep = ",")
df_boxplotModel['Corr']=np.round(df_boxplotModel['Corr'], 2) 
sns.set_theme(style="whitegrid");
#sns.set(font_scale=1.2)
f, ax = plt.subplots(figsize=(9, 6))    
ax = sns.boxplot(x='Model', y='Corr', data=df_boxplotModel, palette="Set1", showfliers=False)
#ax.set_facecolor('white')
ax.set_xticklabels(ax.get_xticklabels(),rotation=30)
ax.set_ylim([0.10,0.75])# add stripplot
ax = sns.stripplot(x='Model', y='Corr', data=df_boxplotModel, color="orange", jitter=0.25, size=5.0)
plt.show()
plt.savefig('/Analysis/BoxPlotModel/Plots/ResultTrainCorrModelLoc1_boxplot.png')

# plotting boxplot for correlation test results on the loc2
df_boxplotModel = pd.read_csv('Analysis/BoxPlotModel/resultDatasets/ResultTrainCorrModelLoc2_boxplot.csv', header = 0, sep = ",")
sns.set_theme(style="whitegrid");
#sns.set(font_scale=1.2)
f, ax = plt.subplots(figsize=(9, 6))    
ax = sns.boxplot(x='Model', y='Corr', data=df_boxplotModel, palette="Set1", showfliers=False)
#ax.set_facecolor('white')
ax.set_xticklabels(ax.get_xticklabels(),rotation=30)
ax.set_ylim([0.10,0.75])# add stripplot
ax = sns.stripplot(x='Model', y='Corr', data=df_boxplotModel, color="orange", jitter=0.25, size=5.0)
plt.show()
plt.savefig('/Analysis/BoxPlotModel/Plots/ResultTrainCorrModelLoc2_boxplot.png')

# plotting boxplot for correlation test results on the loc3
df_boxplotModel = pd.read_csv('Analysis/BoxPlotModel/resultDatasets/ResultTrainCorrModelLoc3_boxplot.csv', header = 0, sep = ",")
df_boxplotModel['Corr']=np.round(df_boxplotModel['Corr'], 2) 
sns.set_theme(style="whitegrid");
#sns.set(font_scale=1.2)
f, ax = plt.subplots(figsize=(9, 6))    
ax = sns.boxplot(x='Model', y='Corr', data=df_boxplotModel, palette="Set1", showfliers=False)
#ax.set_facecolor('white')
ax.set_xticklabels(ax.get_xticklabels(),rotation=30)
ax.set_ylim([0.10,0.75])# add stripplot
ax = sns.stripplot(x='Model', y='Corr', data=df_boxplotModel, color="orange", jitter=0.25, size=5.0)
plt.show()
plt.savefig('/Analysis/BoxPlotModel/Plots/ResultTrainCorrModelLoc3_boxplot.png')


#feature selection wise: plotting boxplot of train and test results of the loc1, loc2 and loc3 datasets
#plotting boxplot for correlation test results on the loc1
df_boxplotModel = pd.read_csv('Analysis/BoxPlotFeatureSelection/resultDatasets/ResultTestCorrLoc1_FS_boxplot.csv', header = 0, sep = ",")
df_boxplotModel['Corr']=np.round(df_boxplotModel['Corr'], 2) 
sns.set_theme(style="whitegrid");
#sns.set(font_scale=1.2)
f, ax = plt.subplots(figsize=(7, 4))    
ax = sns.boxplot(x='FeatureSelection', y='Corr', data=df_boxplotModel, palette="Set1", showfliers=False)
ax.set_xticklabels(ax.get_xticklabels(),rotation=30)
ax.set_ylim([0.10,0.75])
# add stripplot
ax = sns.stripplot(x='FeatureSelection', y='Corr', data=df_boxplotModel, color="orange", jitter=0.25, size=5.0)
plt.show()
plt.savefig('/Analysis/BoxPlotFeatureSelection/Plots/ResultTestCorrLoc1_FS_boxplot.png')


# plotting boxplot for correlation test results on the loc2
df_boxplotModel = pd.read_csv('Analysis/BoxPlotFeatureSelection/resultDatasets/ResultTestCorrLoc2_FS_boxplot.csv', header = 0, sep = ",")
df_boxplotModel['Corr']=np.round(df_boxplotModel['Corr'], 2) 
sns.set_theme(style="whitegrid");
#sns.set(font_scale=1.2)
f, ax = plt.subplots(figsize=(7, 4))    
ax = sns.boxplot(x='FeatureSelection', y='Corr', data=df_boxplotModel, palette="Set1", showfliers=False)
ax.set_xticklabels(ax.get_xticklabels(),rotation=30)
ax.set_ylim([0.10,0.75])
# add stripplot
ax = sns.stripplot(x='FeatureSelection', y='Corr', data=df_boxplotModel, color="orange", jitter=0.25, size=5.0)
plt.show()
plt.savefig('/Analysis/BoxPlotFeatureSelection/Plots/ResultTestCorrLoc2_FS_boxplot.png')


# plotting boxplot for correlation test results on the loc3
df_boxplotModel = pd.read_csv('Analysis/BoxPlotFeatureSelection/resultDatasets/ResultTestCorrLoc3_FS_boxplot.csv', header = 0, sep = ",")
df_boxplotModel['Corr']=np.round(df_boxplotModel['Corr'], 2) 
sns.set_theme(style="whitegrid");
#sns.set(font_scale=1.2)
f, ax = plt.subplots(figsize=(7, 4))    
ax = sns.boxplot(x='FeatureSelection', y='Corr', data=df_boxplotModel, palette="Set1", showfliers=False)
ax.set_xticklabels(ax.get_xticklabels(),rotation=30)
ax.set_ylim([0.10,0.75])
# add stripplot
ax = sns.stripplot(x='FeatureSelection', y='Corr', data=df_boxplotModel, color="orange", jitter=0.25, size=5.0)
plt.show()
plt.savefig('/Analysis/BoxPlotFeatureSelection/Plots/ResultTestCorrLoc3_FS_boxplot.png')


# plotting boxplot for correlation train results on the loc1
df_boxplotModel = pd.read_csv('Analysis/BoxPlotFeatureSelection/resultDatasets/ResultTrainCorrLoc1_FS_boxplot.csv', header = 0, sep = ",")
df_boxplotModel['Corr']=np.round(df_boxplotModel['Corr'], 2) 
sns.set_theme(style="whitegrid");
#sns.set(font_scale=1.2)
f, ax = plt.subplots(figsize=(7, 4))    
ax = sns.boxplot(x='FeatureSelection', y='Corr', data=df_boxplotModel, palette="Set1", showfliers=False)
ax.set_xticklabels(ax.get_xticklabels(),rotation=30)
ax.set_ylim([0.10,0.90])
# add stripplot
ax = sns.stripplot(x='FeatureSelection', y='Corr', data=df_boxplotModel, color="orange", jitter=0.25, size=5.0)
plt.show()
plt.savefig('/Analysis/BoxPlotFeatureSelection/Plots/ResultTrainCorrLoc1_FS_boxplot.png')


# plotting boxplot for correlation train results on the loc2
df_boxplotModel = pd.read_csv('Analysis/BoxPlotFeatureSelection/resultDatasets/ResultTrainCorrLoc2_FS_boxplot.csv', header = 0, sep = ",")
df_boxplotModel['Corr']=np.round(df_boxplotModel['Corr'], 2) 
sns.set_theme(style="whitegrid");
#sns.set(font_scale=1.2)
f, ax = plt.subplots(figsize=(7, 4))    
ax = sns.boxplot(x='FeatureSelection', y='Corr', data=df_boxplotModel, palette="Set1", showfliers=False)
ax.set_xticklabels(ax.get_xticklabels(),rotation=30)
ax.set_ylim([0.10,0.90])
# add stripplot
ax = sns.stripplot(x='FeatureSelection', y='Corr', data=df_boxplotModel, color="orange", jitter=0.25, size=5.0)
plt.show()
plt.savefig('/Analysis/BoxPlotFeatureSelection/Plots/ResultTrainCorrLoc2_FS_boxplot.png')


# plotting boxplot for correlation test results on the loc3
df_boxplotModel = pd.read_csv('Analysis/BoxPlotFeatureSelection/resultDatasets/ResultTrainCorrLoc3_FS_boxplot.csv', header = 0, sep = ",")
df_boxplotModel['Corr']=np.round(df_boxplotModel['Corr'], 2) 
sns.set_theme(style="whitegrid");
#sns.set(font_scale=1.2)
f, ax = plt.subplots(figsize=(7, 4))    
ax = sns.boxplot(x='FeatureSelection', y='Corr', data=df_boxplotModel, palette="Set1", showfliers=False)
ax.set_xticklabels(ax.get_xticklabels(),rotation=30)
ax.set_ylim([0.10,0.90])
# add stripplot
ax = sns.stripplot(x='FeatureSelection', y='Corr', data=df_boxplotModel, color="orange", jitter=0.25, size=5.0)
plt.show()
plt.savefig('/Analysis/BoxPlotFeatureSelection/Plots/ResultTrainCorrLoc3_FS_boxplot.png')