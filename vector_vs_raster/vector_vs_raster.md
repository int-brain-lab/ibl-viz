# Vector vs Raster

I've noticed over the last year that there tends to be a bit of confusion among people about why figures end up really large/small depending on the file type you use. So I thought it would be helpful to share a few tips here. For people in the BWM and Repro Ephys groups, and the future Ephys Atlas and other new task forces I hope this will save you some time in the future when you are generating figures.

tl;dr - to make small figures: save images as PNG, save plots as SVG or PDF, combine png+svg panels into multi-panel figures using illustrator and save as a PDF

Here's another useful description of raster vs. vector graphics from [Adobe's website](https://www.adobe.com/creativecloud/file-types/image/comparison/raster-vs-vector.html).

## There are two ways to save images on a computer

### Raster images

A **raster** image is an image represented by individual pixels, where each pixel has a color.

- You're already familiar with raster images from using cameras
- Common filetypes are JPG and PNG, if you have an iPhone you've probably also seen the new HEIC format, there are many others
- Raster images are the correct format for images, e.g. histology slices, 2-photon data, etc
- Raster images have a resolution, like 1024x800
- Each pixel in the 1024x800 matrix has a color associated with it. At it's most basic an RGB image using one byte per color channel has a total size of 1024x800x32 bytes, or 26 MB. Formats like PNG use compression algorithms to reduce this, without losing any information.
- The standard in 2023 is to use the PNG filetype for raster images
- It's generally only possible to *further* compress a raster if you are willing to give up some information. You can (1) lower the resolution. Or (2) throw out color or spatial information that is hard for the human visual system to see. Option #2 is how JPG works, it compresses images by throwing out information that we can't see visually, but that data will be gone forever.
- Programs like Photoshop, Photopea, and Windows Paint all work with raster images

### Vector graphics

A **vector** graphic is an image represented by lines and polygons, where each shape has a color.

- You might be less familiar with this kind of format, as it only gets used by particular programs
- Common filetypes are SVG, EPS, and in some cases PDF
- Vector graphics are the correct format for almost all scientific figures generated from Python or MATLAB code, if you save from matplotlib, seaborn, or the print command in MATLAB with a SVG or PDF filetype, you will get a vector graphic
- Vector graphics have **no resolution**, you can scale them up or down without changing the file size.
- Inside the file, a vector graphic is just a list of points, polygons created by linking points, and colors, so in some cases the file sizes can be very small despite displaying very complex visuals
- The standard in 2023 is to use either SVG or PDF
- It's generally not possible to compress a vector graphic, there are situations where shapes are overspecified and can be compressed, but these are rare
- Programs like Illustrator and Inkscape work with vector graphics

A small sidenote: have you ever noticed that presentations created in Keynote tend to just look a lot better than presentations in Google Slides or Powerpoint? One reason is that Keynote has always allowed you to insert vector graphics directly in the slides, which makes them look perfectly crisp on the projector! I think recent versions of Powerpoint now allow this as well.

### Converting filetypes

You can always *rasterize* a vector graphic into a raster image. This converts the polygons and colors into pixels at a particular resolution. In general, for scientific plots this will result in a larger file size and is a bad idea.

The reverse is not true, it's difficult to *vectorize* a raster image, unless the image is very simple.

### Some examples

Here is a really basic vector graphic that I put together in Illustrator

![vector graphic](./basic_vector.svg "Basic Vector as SVG")

This vector graphic is **tiny** at 797 bytes and can scale to any arbitrary resolution! Here is what's actually in this file:

```
<?xml version="1.0" encoding="utf-8"?>
<!-- Generator: Adobe Illustrator 27.2.0, SVG Export Plug-In . SVG Version: 6.00 Build 0)  -->
<svg version="1.1" id="Layer_1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" x="0px" y="0px"
	 viewBox="0 0 250 250" style="enable-background:new 0 0 250 250;" xml:space="preserve">
<style type="text/css">
	.st0{fill:#DC1D42;stroke:#FFFFFF;stroke-miterlimit:10;}
	.st1{fill:#3A4A9F;stroke:#FFFFFF;stroke-miterlimit:10;}
	.st2{fill:#50B848;stroke:#FFFFFF;stroke-miterlimit:10;}
</style>
<rect x="27.42" y="30.57" class="st0" width="77.12" height="65.02"/>
<circle class="st0" cx="122.78" cy="165.47" r="18.24"/>
<circle class="st1" cx="156.78" cy="113.83" r="18.24"/>
<circle class="st2" cx="189.59" cy="165.47" r="18.24"/>
</svg>
```

That's it! That file could even be compressed further by removing some of the unnecessary header information where Illustrator is advertising itself. If we re-save this file as a 250x250 pixel PNG:

![png image](./basic_vector.png "Basic Vector as PNG")

It now takes up 20KB, 20x more. If you zoom in, you'll also see that there are now compression artifacts around the edges of the circles while the vector graphic is perfectly crisp when you zoom in.

If this was saved as a Bitmap (BMP) file with no compression, it would require 250x250x32 bits, or 2MB. So the PNG compression algorithm for this simple image gives us about 100x compression.

Here's now a more complex image:

![complex png image](./bwm_angled.png "BWM Angled as PNG")

This PNG file is quite complex and large, at 1572x1441 pixels. It's technically possible to vectorize an image like this one, which has fairly large chunks of colors, into a vector graphic. If we do that we get this:

![complex vector graphic (from png)](./bwm_angled.svg "BWM Angled as SVG")

Note that this looks pretty bad compared to the original image, we've basically done a form of very bad compression on the image. This file is also actually *larger* than the original image. A great example that once you've gone to a raster image you generally can't (and shouldn't!) go back to a vector graphic!

## Building scientific figures

An important thing to note is that **PDF** files can contain both vector and raster elements in them. This is really useful for us, since in scientific figures for papers we often want to show both images of our raw data (such as histology) alongside scatterplots, barplots, etc, which are all easily represented as vectors.

If you are trying to make your figures as small as possible, the general steps to do this are:

1. Save all figure panels from Python/MATLAB as vector graphics (SVG, or PDF if they have text). You may need to specify a resolution when you save your file, but this is actually somewhat arbitrary as you can scale them up or down later as needed.
2. Save images (histology, raw imaging data, etc) as rasters (PNG) at high resolution. In general you want at least 300 pixels per inch for the final printed output. For a one-column panel of a 4-column figure, intended to be read on regular printer paper (8.5"), you will need to have at least 500x500 pixels to meet that standard.

That's it. Don't do any compression at this point!

### Compiling multi-panel figures

When compiling multi-panel figures, you can either do this in code or use either InDesign or Illustrator (or comparable programs). Make sure to save to the PDF filetype, the program will correctly keep vectors as vectors and rasters as rasters.

You'll know that this worked if the total filesize of your multi-panel figure is more or less the same as the sum of the file sizes of the individual panels. A PDF is really just a bucket where you can combine elements, it only adds a few extra bytes of additional header information on top.

### Troubleshooting

If your final multi-panel PDF is too large, the most likely offenders are any raster images you included. Before reducing the resolution, try running them through a visual compression algorithm (e.g. using tinypng.com), but *make sure to keep a backup of the original* since any compression you do will cause permanent loss of information. Visual compression algorithms try to discard information that humans can't see anyways. If visual compression fails to make enough of a reduction in file size, then reduce the resolution.

Figures rendered as vector graphics should be relatively small in size. There are a few situations where you might get very large file sizes from vector graphics, usually when you are exporting something that is basically an image, e.g. anything with a continuous color gradient. A very large file size on a vector graphic means that it's basically an image and that you should try rasterizing it. Either re-save the figure as a PNG file from Python/MATLAB. Or using Illustrator, select `File > Export As` and export the file to a PNG with sufficient resolution (300+ pixels per inch).

If your individual panels can't be compressed enough to make the final multi-panel figure small then come get help from your visualization team!

**One final but important note:** Converting a mixed vector/raster PDF that came out of InDesign/Illustrator to a raster image is a *bad idea* and will only make the file larger while reducing the quality of the figure. Don't do this!
