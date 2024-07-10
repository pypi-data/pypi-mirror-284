from . GenomeTrack import GenomeTrack
from . BedTrack import BedTrack
from .. readGtf import ReadGtf
from matplotlib import font_manager
from .. utilities import temp_file_from_intersect
import numpy as np

DEFAULT_BED_COLOR = '#1f78b4'
DISPLAY_BED_VALID = ['collapsed', 'triangles', 'interleaved', 'stacked', 'squares', 'deletions', 'inversions']
DISPLAY_BED_SYNONYMOUS = {'interlaced': 'interleaved', 'domain': 'interleaved'}
DEFAULT_DISPLAY_BED = 'stacked'
AROUND_REGION = 100000


class GtfTrack(BedTrack):
    SUPPORTED_ENDINGS = ['gtf', 'gtf.gz']
    TRACK_TYPE = 'gtf'
    OPTIONS_TXT = GenomeTrack.OPTIONS_TXT + f"""
# By default the transcript_name is used.
# If you want to use the gene_name:
prefered_name = gene_name
# By default, the gtf is transformed to transcripts
# If you want to use see only one structure per gene
# merge_transcripts = true
# Sometimes merging transcripts without merging overlapping
# exons may give unexpected output especially when
# multiple 3' exons overlap. We recommand to use:
# merge_overlapping_exons = true
# You can change the color of coding sequences by:
color = darkblue
# optional: line_width
#line_width = 0.5
# optional: border_color
# default is black.
# To remove the border, simply set 'border_color' to none
# Not used in tssarrow style
#border_color = black
# the display parameter defines how the gtf file is plotted.
# Default is 'stacked' where regions are plotted on different lines so
# we can see all regions and all labels.
# The other options are ['collapsed', 'interleaved', 'triangles', 'squares', 'deletions', 'inversions']
# These 2 last options assume that the regions do not overlap:
# `collapsed`: The gtf regions are plotted one after the other in one line.
# `interleaved`: The gtf regions are plotted in two lines, first up, then down, then up etc.
# style to plot the genes when the display is 'stacked', 'collapsed' or 'interleaved'
#style = UCSC
#style = flybase
#style = tssarrow
#style = exonarrows
# maximum number of gene rows to be plotted. This
# field is useful to limit large number of close genes
# to be printed over many rows. When several images want
# to be combined this must be set to get equal size
# otherwise, on each image the height of each gene changes
#gene_rows = 10
# by default the ymax is the number of
# rows occupied by the genes in the region plotted. However,
# by setting this option, the global maximum is used instead.
# This is useful to combine images that are all consistent and
# have the same number of rows.
#global_max_row = true
# whether printing the labels
labels = false
# optional:
# by default the labels are not printed if you have more than 60 features.
# to change it, just increase the value:
#max_labels = 60
# optional: font size can be given to override the default size
fontsize = 10
# If you want to plot all labels inside the plotting region:
#all_labels_inside = true
# If you want to display the name of the gene which goes over the plotted
# region in the right margin put:
#labels_in_margin = true
# If you want to use italic for your labels:
#fontstyle = italic
# if you use UCSC or exonarrows style, you can set the relative distance between 2 arrows on introns/exons
# default is 2
#arrow_interval = 2
# you can also choose the color of arrows
# default is black
#color_arrow = black
# if you use tssarrow style, you can choose the length of the arrow in bp
# (default is 4% of the plotted region)
#arrow_length = 5000
# if you use flybase, tssarrow or exonarrows style, you can choose the color of non-coding intervals:
#color_utr = grey
# for flybase and tssarrow, you can choose the proportion between their height and the one of coding
# (by default they are the same height):
#height_utr = 1
# if you use flybase or UCSC style, you can choose the color of the backbone
#color_backbone = red
# By default, for oriented intervals in flybase style,
# the arrowhead is added
# outside of the interval.
# If you want that the tip of the arrow correspond to
# the extremity of the interval use:
#arrowhead_included = true
# By default the size of this arrow is 0.4% of the plotted region.
# This size is also used to put space between the gtf regions and
# their labels.
# To increase it:
#arrowhead_fraction = 0.01
# for exonarrows, you can choose the proportion between the height of the introns and the one of exon
# (by default introns are half):
#height_intron = 0.5
# The two following display options are really different and no label can be display:
# `triangles` display each region as a triangle, can be useful to overlay with a hic_matrix
# `squares` display each region as a square along the diagonal, can be useful to overlay with a hic_matrix_square
# The 2 last display options do not expect overlapping feature:
# `deletions` display a line on the plotted region (color can be controlled by color_backbone)
# and a V shape breaking the line for each region in bed (color can be controled by color)
# `inversions` display 2 arrows around each region
# For both, labels can be displayed on bottom centered on the region
# optional. If not given is guessed from the file ending.
file_type = {TRACK_TYPE}
    """

    DEFAULTS_PROPERTIES = {'fontsize': 12,
                           'orientation': None,
                           'color': DEFAULT_BED_COLOR,
                           'border_color': 'black',
                           'labels': True,
                           'style': 'flybase',
                           'display': DEFAULT_DISPLAY_BED,
                           'line_width': 0.5,
                           'max_labels': 60,
                           'prefered_name': 'transcript_name',
                           'merge_transcripts': False,
                           'merge_overlapping_exons': False,
                           'global_max_row': False,
                           'gene_rows': None,
                           'arrow_interval': 2,
                           'arrowhead_included': False,
                           'arrowhead_fraction': 0.004,
                           'color_utr': 'grey',
                           'color_backbone': 'black',
                           'height_utr': 1,
                           'region': None,  # Cannot be set manually but is set by tracksClass
                           'arrow_length': None,
                           'height_intron': 0.5,
                           'all_labels_inside': False,
                           'labels_in_margin': False,
                           'fontstyle': 'normal',
                           'color_arrow': 'black'}
    NECESSARY_PROPERTIES = ['file']
    SYNONYMOUS_PROPERTIES = {'display': DISPLAY_BED_SYNONYMOUS}
    POSSIBLE_PROPERTIES = {'orientation': [None, 'inverted'],
                           'style': ['flybase', 'UCSC', 'tssarrow', 'exonarrows'],
                           'display': DISPLAY_BED_VALID,
                           'fontstyle': ['normal', 'italic', 'oblique']}
    BOOLEAN_PROPERTIES = ['labels', 'global_max_row',
                          'arrowhead_included', 'all_labels_inside',
                          'labels_in_margin',
                          'merge_transcripts', 'merge_overlapping_exons']
    STRING_PROPERTIES = ['file', 'file_type',
                         'overlay_previous', 'orientation',
                         'title', 'style', 'color', 'border_color',
                         'color_utr', 'display', 'fontstyle',
                         'color_backbone', 'color_arrow',
                         'prefered_name']
    FLOAT_PROPERTIES = {'fontsize': [0, np.inf],
                        'line_width': [0, np.inf],
                        'height': [0, np.inf],
                        'height_utr': [0, 1],
                        'height_intron': [0, 1],
                        'arrowhead_fraction': [0, np.inf]}
    INTEGER_PROPERTIES = {'gene_rows': [0, np.inf],
                          'max_labels': [0, np.inf],
                          'arrow_interval': [1, np.inf],
                          'arrow_length': [0, np.inf]}

    def set_properties_defaults(self):
        super(BedTrack, self).set_properties_defaults()
        self.fp = font_manager.FontProperties(size=self.properties['fontsize'])
        self.colormap = None
        # check if the color given is a color map
        # Contrary to bed it cannot be a colormap
        self.process_color('color', colormap_possible=False,
                           bed_rgb_possible=False,
                           default_value_is_colormap=False)

        # check if border_color and color_utr and color_backbone are colors
        # if they are part of self.properties
        # (for example, TADsTracks do not have color_utr nor color_backbone)
        for param in [p for p in ['border_color', 'color_utr', 'color_backbone', 'color_arrow']
                      if p in self.properties]:
            self.process_color(param, bed_rgb_possible=False)

        # to set the distance between rows
        self.row_scale = 2.3

    def get_bed_handler(self, plot_regions=None):
        if not self.properties['global_max_row']:
            # I do the intersection:
            file_to_open = temp_file_from_intersect(self.properties['file'],
                                                    plot_regions, AROUND_REGION)
        else:
            file_to_open = self.properties['file']

        bed_file_h = ReadGtf(file_to_open,
                             self.properties['prefered_name'],
                             self.properties['merge_transcripts'],
                             self.properties['merge_overlapping_exons'])
        total_length = bed_file_h.length
        return bed_file_h, total_length
