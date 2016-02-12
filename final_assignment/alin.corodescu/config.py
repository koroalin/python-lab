{
    "before_install": 
    [
    	{
            "download": 
            {
                "source": "https://localhost/file",
                "destination": "/home/alex/script.sh",
        	}
    	},
	],
    "install": 
    [
    	{
            "run_script": 
            {
            	# How many times to retry running the command.
                "attempts": 3,
         	   # Single bool, int, or list of allowed exit codes.
                "check_exit_code": True,
            	# The command passed to the command runner.
                "command": "bash /home/alex/script.sh",
            	# Set the current working directory
                "cwd": "/home/alex/",
            	# Environment variables and their values that
            	# will be set for the process.
                "env_variables": {"tuxy": "Tuxy Pinguinescu"},
            	# Interval between execute attempts, in seconds.
                "retry_interval": 3,
            	# Whether or not there should be a shell used to
            	# execute this command.
                "shell": True,
        	},
        	# ...
    	}
	],
    "after_install": 
    [
    	{
            "reboot": 
            {
                "method": "soft",
        	}
    	}
	],
 
    "install_failed": 
    [
    	{
            "delete": 
            {
                "method": "force",
                "path": "/home/alex"
        	},
    	},

    	{
            "shutdown": 
            {
                "method": "hard",
        	},
    	},
	],
    "config": 
    {
        "hostname": "TuxyNode-1",
        "users": 
        {
            "acoman": 
            {
                "full_name": "Alexandru Coman",
                "primary-group": "admin",
                "groups": ["users"],
                "expiredate": "2016-09-01",
                "password": ""
        	},
        	# ...
    	},
        "write_files": 
        {
        	0: 
            {
                "path": "/home/alex/test",
                "permissions": "0555",
                "encoding": "gzip",
                "content": "",
        	},
    	},
	}
}