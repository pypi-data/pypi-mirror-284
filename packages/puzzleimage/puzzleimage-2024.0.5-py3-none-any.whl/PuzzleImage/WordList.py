import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

class WordList:
    def __init__(self, words, width, height, fontsize, draw_box=True, draw_label=True, draw_labelline=True, draw_copyright=True, copyright_fontname=None):
        self.width = width
        self.height = height
        self.fontsize = fontsize
        self.draw_box = draw_box
        self.draw_label = draw_label
        self.draw_labelline = draw_labelline
        self.draw_copyright = draw_copyright
        self.copyright_fontname = copyright_fontname
        self.inch_of = lambda size: size / 72
        self.words = np.array(sorted(words, key=lambda word: (len(word), word)))
        self.w_num = len(self.words)
        self.row_num = int(height / self.inch_of(fontsize) * 19 / 28)
        self.char_max_per_row = int(height / self.inch_of(fontsize)) - 1
        self.col_num = int(np.ceil(self.w_num / self.row_num))
        if self.w_num != 0:
            self.w_lens = np.vectorize(len)(self.words)
            # redefine row number
            self.row_num = int(np.ceil(self.w_num / self.col_num))  # row number


    def draw_wordlist(self, ax):
        ax.set(xlim=(0, self.width), ylim=(0, self.height))
        ax.axis("off")

        if self.w_num == 0:
            return ax
            
        # write list
        box = {
            "fc": "#f5efe6", # facecolor
            "ec": "darkgray", # edgecolor
            "style": mpatches.BoxStyle("Round", pad=0.05*self.fontsize/30),
            "size": 0.15 * self.fontsize / 30,
            "difx": 0.3 * self.fontsize / 30, # difference from word_x to draw box
            "dify": 0.25 * self.fontsize / 30, # difference from word_y to draw box
        }
        label = {
            "difx": 0.55* self.fontsize / 30, # difference from word_x to draw the label
            "dify": 0.2 * self.fontsize / 30, # difference from word_y to draw the label
            "size": 14 * self.fontsize / 30, # label font size
            "color": "dimgray",
        }
        labelline = {
            "difx": 0.45 * self.fontsize / 30, # difference from word_x to draw the label line
            "width": 3 * self.fontsize / 30, # line width
            # "space": self.char_max_per_row / (int(self.height / self.inch_of(self.fontsize)) - 6),
            "space": 1.4,
            "ymin_dif": self.inch_of(self.fontsize) * 0.8 , # coefficient of ymin when drawing a label
            "ymax_dif": 0.05 * self.fontsize / 30 # coefficient of ymax when drawing a label
        }
        

        # k: array number of words, j: column number, i: row number
        k = 0
        word_x = self.inch_of(self.fontsize) * 2
        ymax_default = (self.height * 0.995 - labelline["ymax_dif"]) / self.height
        for j in range(self.col_num):
            if j > 0:
                word_x += (self.w_lens[self.row_num * j] + 3.5) * self.inch_of(self.fontsize)
            ymax = ymax_default
            for i in range(self.row_num):
                if k == self.w_num:
                    break
                word_y = self.height * 0.995 - i * self.inch_of(self.fontsize) * labelline["space"]
                # box
                if self.draw_box is True:
                    fancybox = mpatches.FancyBboxPatch((word_x-box["difx"], word_y-box["dify"]), box["size"], box["size"], boxstyle=box["style"], fc=box["fc"], ec=box["ec"], alpha=1)
                    ax.add_patch(fancybox)

                # main word
                ax.text(word_x, word_y, self.words[k], size=self.fontsize, ha="left", va="top")

                # label
                if self.draw_label is True:
                    if k == 0 or self.w_lens[k] > self.w_lens[k-1]:
                        ax.text(word_x-label["difx"], word_y-label["dify"], str(self.w_lens[k]), fontsize=label["size"], color=label["color"], ha="right")
                
                # label line
                if self.draw_labelline is True:
                    if i != 0 and self.w_lens[k] > self.w_lens[k-1]:
                        ymin = (self.height * 0.995 - (i-1) * self.inch_of(self.fontsize) * labelline["space"] - labelline["ymin_dif"]) / self.height
                        ax.axvline(x=word_x-labelline["difx"], color="lightgray", ymin=ymin, ymax=ymax, lw=labelline["width"])
                        ymax = (word_y - labelline["ymax_dif"]) / self.height
                k += 1
            if self.draw_labelline is True:
                if j == self.col_num-1 and k == self.w_num and self.w_num%self.row_num != 0 :
                    ymin = (self.height*0.995 - self.inch_of(self.fontsize) * (i-1) * labelline["space"] - labelline["ymin_dif"]) / self.height
                else:
                    ymin = (self.height*0.995 - self.inch_of(self.fontsize) * (i) * labelline["space"] - labelline["ymin_dif"]) / self.height
                ax.axvline(x=word_x-labelline["difx"], color="lightgray", ymin=ymin, ymax=ymax, lw=labelline["width"])            

        if self.draw_copyright is True:
            # ax.text(self.width, 0, '© MakePuzz', size=self.fontsize, ha='right', va='bottom', fontname=self.copyright_fontname, alpha=0.5, fontweight='bold')
            ax.text(ax.texts[-1].get_position()[0], 0, '© MakePuzz', size=self.fontsize, ha='left', va='bottom', fontname=self.copyright_fontname, alpha=0.5, fontweight='bold')
        return ax

    def cal_width(self):
        word_x = self.inch_of(self.fontsize) * 2
        for j in range(self.col_num):
            if j > 0:
                word_x += (self.w_lens[self.row_num * j] + 2) * self.inch_of(self.fontsize)
        word_x += (self.w_lens[self.w_num - 1]) * self.inch_of(self.fontsize)
                
        return word_x
