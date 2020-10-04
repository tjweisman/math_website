% Math network access

Accessing your math department files
====================================

There's a lot of information on this page. Some shortcuts:

- I just want to [update my website *now*](network_access.html#web-access)

- I want to know an [easy way](network_access.html#other-client) to update my website regularly

- I want to [use the command line](network_access.html#command-line)

Remember your website lives in the "public_html" folder in your home directory. Whatever you put in there can be accessed at the link:

	https://web.ma.utexas.edu/users/[your username]

If you're a first-year, your username is probably just your EID. If you're not a first-year, your username is probably the part of your UT email address before the "@" sign.

The instructions on this page are for accessing your files on the math department network. If you want to update your *directory page* on the *math department website*, [log on](https://www.ma.utexas.edu/log-on-off) at the math department website and then follow the instructions [here](https://www.ma.utexas.edu/my-profile/activate-my-directory-entry).

--------------------------------------------------------

## Accessing your files through the web <a name="web-access"></a>

The web interface can be found at this link: <a href="https://web.ma.utexas.edu/horde/gollem/manager.php?backend_key=ssh2" target="_blank">https://web.ma.utexas.edu/horde/gollem/manager.php?backend_key=ssh2</a>

**You need to log in *twice* to get this to work.**

1. First login: make sure that the *Server* is set to **UTM**. Then, under "UTM username" and "UTM password," enter your **math department network username** and **math department network password.**

2. Second login: the prompt asks you for a username and password. Again, enter your **math department network username** and your **math department network password**.

3. If all goes well you should have a web interface for uploading/managing files in your home folder.

If Step 1 doesn't work for some reason: try setting the server to **Office365**, and then enter your **UT email address** and **UT EID password**. Then follow Step 2 as before. 

### Getting to the web interface from the [math department website](https://www.ma.utexas.edu/)

If you want to know how to get to the interface without having to go to this page first:

1. Go to [Quick Links for UT Math](https://www.ma.utexas.edu/services/quick-links#ut-links) at the bottom of the page.
2. Click on [Access your files on Math network](https://web.ma.utexas.edu/horde/login.php) on the list.
3. Log in via the Horde client using your **math department username and password** (see step 1 above).
4. In the top menu, go to Others => File Manager. This takes you to the link given above.
5. Log in again using your **math department username and password.**

-------------------------------------------------------

## Using another client <a name="other-client"></a>

Using the web interface is a pain and if you plan to update your website regularly, you can save yourself some trouble by using a different client.

If you're on Windows, you can try using [WinSCP](https://winscp.net/eng/index.php). [FileZilla](https://filezilla-project.org/) is also free and works on Windows, MacOS, and Linux.

### To use WinSCP:

1. Run WinSCP

2. Under "File Protocol," select *SFTP*.

3. Under *Host name*, enter: *math.utexas.edu*. You can leave the port number set at the default value.

4. Under *Username* and *Password*, enter your **math department username and password**.

5. Click "Login."

You will likely get a popup warning you that you are connecting to an untrusted host. *This is ok* - your computer is just telling you that you're connecting to the math network remotely for the first time and wants to make sure you're aware. [What if I'm paranoid about this?](network_access.html#rsa-fingerprint)

You may also be prompted for two-factor authentication.

You can also save the host/login information (and agree to set the math department network as a "trusted host") so you can connect faster the next time you do this.

You'll then have access to a two-paned interface where you can drag files from your filesystem to your math department home directory and back. You can also set up a single folder to keep synchronized on both machines.

### To use FileZilla:

1. Run FileZilla

2. Under *Host*, enter *sftp://math.utexas.edu*.

3. Under *Username* and *Password*, enter your **math department username and password**.

4. Click "Quickconnect." You can leave the *Port* box blank.

Once again you might get a warning about connecting to an [untrusted host](network_access.html#rsa-fingerprint).

FileZilla also will let you save your login information. You might be prompted for two-factor authentication.
 
----------------------------------------------------------

# More complicated options <a name="command-line"></a>

You can stop reading now if you don't want to use a command line to solve your problems.

## Using SSH on the command line

If you're on MacOS or Linux, or you're running an updated version of Windows 10, you probably have a native SSH client already. If you're running an older version of Windows, you will want to use [PuTTY](network_access.html#putty).

To SSH into the math department network, run the following command at a terminal (*[username]* is your **math department username**):

	ssh [username]@math.utexas.edu

If this is your first time connecting with SSH, you may get a warning about [trusted hosts](network_access.html#rsa-fingerprint).

You'll be prompted to enter two-factor authentication. Then you enter your **math department** password. Once you're in, you can manage your files (and do anything else you would on a math department machine) from the terminal. This will *not* (by itself) let you transfer files back and forth from your local machine, but you can set up some [tools](network_access.html#other-options) from this end that will help you do that.

## Using *scp* to transfer a single file

If you just want to transfer a single file to your math department account, you can use the *scp* command. At a terminal, run:

	scp [file_to_transfer] [username]@math.utexas.edu:~

This transfers the file to your home directory. If you want to transfer a file to a specific folder (say public_html), you can run e.g.

	scp [file_to_transfer] [username]@math.utexas.edu:~/public_html

## Using PuTTY <a name="putty"></a>

If you're running an older version of Windows, and you want to use the command line for SSH tasks, you should install [PuTTY](https://putty.org/).

Once you're running PuTTY, enter *[username]@math.utexas.edu* into the *Host Name* box and make sure you select "SSH" for the connection type. 

If this is your first time connecting, you'll get a warning about [trusted hosts](network_access.html#rsa-fingerprint). You'll then be prompted for two-factor authentication and your **math department** password. Then you'll have access to a remote shell.

If you want to transfer files from the command line using PuTTY scp, you can run

	pscp [file_to_transfer] [username]@math.utexas.edu:~

---------------------------------------------------------

## Setting up SSH keys

You can set up SSH keys so that you don't have to enter your username and password every time you want to SSH into the UT network.

### Using *ssh-keygen*

1. From the command line on your own computer, run the command *ssh-keygen* and follow the prompts.

2. If you've used the default options, you can run the command:

		ssh-copy-id [username]@math.utexas.edu
	
	to copy your public key information to the math network server.

3. To make sure this worked, try running

		ssh [username]@ssh.ma.utexas.edu

You should be able to log in without being prompted for your UT network password or two-factor authentication.

[Much more information about ssh-keygen](https://www.ssh.com/ssh/keygen/)

### Using PuTTYgen

1. From a computer where you have PuTTY installed, run the PuTTYgen program.

2. Click "Generate key" to generate a new key and follow the prompts.

3. Copy the contents of the box labelled "Public key for pasting into OpenSSH authorized_keys file" somewhere you can access it on your math department account.

4. Click "Save private key" and save the private key file you generated. 

5. On your account on the **math department network**, create a new file called *authorized_keys* in the directory *~/.ssh* (this directory is hidden by default, so you may need to do this in the terminal or unhide the directory).

6. Copy the *public key* from step 3 into the *authorized_keys* file.

7. On your own computer, run PuTTY, and navigate to Connection => SSH => Auth. In the box labelled "Private key file for authentication", load the file you saved in step 4.

8. If you save the configuration, you should be able to connect to *[username]@ssh.ma.utexas.edu* via PuTTY.

[More information about PuTTYgen](https://www.ssh.com/ssh/putty/windows/puttygen)

----------------------------------------------------------

## Other options for keeping your website updated <a name="other-options"></a>

### Using rsync

[rsync](https://download.samba.org/pub/rsync/rsync.1) is a command-line tool you can use to synchronize the contents of a directory on your machine with a remote directory. This is what I use to keep my own website updated.

#### Using git

[git](https://git-scm.com/) is a version-control system that's already installed on math department computers and works well on the command-line. You can keep your website in a remote repository (using e.g. [GitHub](https://github.com/)), and pull changes from it to your *public_html* folder.

Alternatively, you can push changes directly to a repository hosted on the math network if you set up the remote manually:

1. From the *public_html* directory on the math department network, run

		git init

	to initialize a new repository. Make whatever initial commits you want.

2. From the *public_html* directory, run

		git config --local receive.denyCurrentBranch updateInstead

3. From your own computer, clone your new repository by running

		git clone [username]@math.utexas.edu:~/public_html

	Now you can make changes to this repository and push them to the math network directly.

If you're already using GitHub to version control your website, you can still set up your math department site as a remote so you can update it directly. Instead of step (3) above, instead run:

	git remote add [remote-name] [username]@math.utexas.edu:~/public_html

You can choose *remote-name* to be whatever you want (say, *website*). You can then push changes to GitHub (or wherever your repository is hosted) by running

	git push

and push changes to the web by running:

	git push [remote-name] master

----------------------------------------------------------

## RSA fingerprints <a name = "rsa-fingerprint"></a>

Your computer keeps track of all of the different hosts you've connected to with SSH, and gives you a warning whenever you connect to one you haven't visited before. You'll be shown the *RSA fingerprint* of the host you're trying to connect with - this is a unique identifier that (hopefully) can't be faked so you can be sure you're connecting to the right network.

The math department's RSA fingerprint is one of:

	bsHWzgwUrN3DNtbymiD9s/og0AjXpjrk65i+5cYPnfY

	4c:c0:4e:8f:c7:ce:97:e4:59:c3:d9:8e:79:fe:cf:13

If you see either of these displayed when you try and connect, you're good to go (of course, this information is only as trustworthy as the website you're reading it on).