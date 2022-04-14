# axis limit:
plt.xlim(0, 56)
ax.set_xlim([0, 100])

# set text:
ax.text(-3, 0.40, '1', color='gray', fontsize = 20)

# modify axis:
ax.axis('off')
ax.set(yticklabels=[])
ax.tick_params(left=False)
sns.despine(left=True)

ax.clear()
ax.plot(np.repeat(stdInPercent,fpm),zorder=1)
ax.set_xticks(np.arange(0, len(score_repeat)+1, fpm))
ax.set_xticklabels(list(np.arange(0, len(score)+1, 1)))
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)
ax.set_yticks(np.arange(0, 101, 20))

