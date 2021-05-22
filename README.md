# ncdisp.py
A Python implementation of MATLAB's [ncdisp](https://www.mathworks.com/help/matlab/ref/ncdisp.html) function.

## Usage

``` python
>>> from ncdisp import ncdisp
>>> ncdisp('example.nc')
```

or

```shell
> python ncdisp.py example.nc
```

```
Source:
	example.nc
Format:
	netcdf4
Global Attributes:
	creation_date = '29-Mar-2010'
Dimensions:
	x = 50
	y = 50
	z = 5
Variables:
	avagadros_number
		Size:       1x1
		Dimensions: 
		Datatype:   float64
		Attributes:
		            description = 'this variable has no dimensions'
	temperature
		Size:       50x1
		Dimensions: x
		Datatype:   int16
		Attributes:
		            scale_factor = 1.8
		            add_offset   = 32.0
		            units        = 'degrees_fahrenheight'
	peaks
		Size:       50x50
		Dimensions: x,y
		Datatype:   int16
		Attributes:
		            description = 'z = peaks(50);'
Groups:
	/grid1/
		Attributes:
			description = 'This is a group attribute.'
		Dimensions:
			x    = 360
			y    = 180
			time = 0	(UNLIMITED)
		Variables:
			temp
				Size:       360x180x0
				Dimensions: x,y,time
				Datatype:   int16
	/grid2/
		Attributes:
			description = 'This is another group attribute.'
		Dimensions:
			x    = 360
			y    = 180
			time = 0	(UNLIMITED)
		Variables:
			temp
				Size:       360x180x0
				Dimensions: x,y,time
				Datatype:   int16
```

## Requirements

`netcdf4>=1.5.6`

## Notes

The `location` and `dispFormat` keywords are not supported yet.
