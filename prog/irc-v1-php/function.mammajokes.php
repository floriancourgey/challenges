<?
	$datafile = "mammajokes.txt";
	
	$mommajokes = file_get_contents($datafile);
	$mommajokes = explode("\n",$mommajokes);
	$mommacount = 0;
	
	// randomize //
	shuffle($mommajokes);
	
	function get_momma_joke()
	{
		global $mommajokes;
		global $mommacount;
		return($mommajokes[$mommacount++]);
	}
?>