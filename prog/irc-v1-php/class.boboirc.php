<?php

error_reporting(E_ALL);

include_once('function.mammajokes.php');


class boboirc
{
	private $fp, $readbuffer, $line, $mcommands;
	public $nick, $ident, $realname, $host, $port;
	
	function boboirc($nick, $ident, $realname, $host, $port)
	{
		$this->nick 		= $nick;
		$this->ident 		= $ident;
		$this->realname = $realname;
		$this->host 		= $host;
		$this->port 		= $port;

		$this->fp = fsockopen($host, $port, $erno, $errstr, 30);
		if(!$this->fp) die("Could not connect\r\n");
		
    	fwrite($this->fp, "NICK ".$nick."\r\n");
    	fwrite($this->fp, "USER ".$ident." ".$host." bla :".$realname."\r\n");

		$this->flush();

	}
	
	function loop()
	{
		// now for program loop //
		while (!feof($this->fp)) 
		{
			$this->line = fgets($this->fp, 256); // wait for a message

			if($this->is_ping($this->line)) $this->pong();
						
			if(strstr($this->line,"PRIVMSG"))
			{
				echo "PRIVMSG...  \r\n";
				// incoming private message //
				$msg = $this->msgToArray($this->line);
								
				// is this a command?
				if($command = $this->get_command($msg['msg']))
				{
					echo "processing command ($command)... \r\n";
					// erase command from message array  // array('from, 'chan', 'msg'); //
					$msg['msg'] = trim(str_replace($command,'',$msg['msg']));
					echo "parsing command ($command)... \r\n";
					$this->parse_command($command, $msg);
				}
			}
			
			$this->line = "";
			$this->flush();
			$this->wait(); // time to next cycle
		}

	}
	
	// outgoing //
	function out($msg) // raw message
	{
		if(@empty($msg)) return false;
		if(!strstr($msg, "\n")) $msg .= "\n";

		fwrite($this->fp, $msg);
		return true;
	}
	
	function setNick($nick)						{ $this->out("NICK ".$nick."\r\n"); $this->nick = $nick; }
	function joinChan($channel) 			{ $this->out("JOIN :".$channel."\r\n"); }
	function quitChan($channel) 			{ $this->out("PART :".$channel."\r\n"); }

	function listChans() 							{ $this->out("LIST\r\n"); }
	function getTopic($channel)				{ $this->out("TOPIC ".$channel."\r\n"); }
	
	function msg($target, $msg) 			{ $this->out("PRIVMSG $target :$msg\r\n"); }
	function msgChan($channel, $msg) 	{ $this->msg($channel, $msg); }
	function msgUser($user, $msg) 		{ $this->msg($user, $msg); }
	
	function pong() 									{ $this->out("PONG :".$this->host."\r\n"); }
	function quit($msg="")						{ $this->out("QUIT :$msg\r\n"); }
	
	// incoming processing //
	function is_ping($line)						{ if(strstr($line, 'PING')) return true; }
	function is_msg($line)						{ if(strstr($line, 'PRIVMSG')) return true; }

	function msgToArray($line) // array('from, 'chan', 'msg');
	{
		$array = explode(":",$line);
				
		$from = explode("!",$array[1]);
		$from = trim($from[0]);
		
		$fromchan = explode("#",$array[1]);
		$fromchan = "#".trim($fromchan[1]);
		
		$string = $array[2];
		$string = trim($string);
		
		$msg = array('from'=>$from, 'chan'=>$fromchan, 'msg'=>$string);
		
		return $msg;
	}
	
	// system
	function flush()									{ @ob_flush; @flush(); }
	function wait()										{ usleep(100000); }
	function get_command($string)
	{
		if(!strstr($string,"!")) return false;
		if(!strstr($string, " "))
			$command = $string;
		else
		{
			$command = explode(" ", $string,2);
			$command = $command[0];
		}
		return $command;
	}
	
	// misc useful functions //
	function rem_xs_whitespace($string){ $string = trim(preg_replace('/\s+/', ' ', 	$string)); return $string; }



	// command parser //
	// TELL THE PARSER WHAT COMMANDS ARE AVAILABLE
	// add commands in the next section below this function
	function parse_command($command, $msg)
	{
		// $command = "!command"; $msg = array('from, 'chan', 'msg')
		switch($command)
		{
			case '!sayrand'	: $this->command_sayrand($msg); break;
			// example plugin
			case '!yomama'	: $this->command_mamajoke($msg); break;
		}
	}
	
	// now for commands //
	// ADD YOUR COMMANDS BELOW //
	function command_sayrand($msg)
	{
		$number = rand(1,100);
		$this->msgChan($msg['chan'], "random number:".$number);
		echo "saying magic number...\r\n";
	}

	function command_math($msg)
	{
		$m = new EvalMath;
		$this->msgChan($msg['chan'], "math:".$m->e($msg['msg']));
		echo "calculating some math...\r\n";
	}
	
	function command_mamajoke($msg)
	{
		//get_momma_joke()
		$this->msgChan( $msg['chan'], get_momma_joke() );
		echo "mama joke...\r\n";
	}
}

?>