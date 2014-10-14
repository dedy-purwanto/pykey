|ImageLink|_ |ImageLink2|_

.. |ImageLink| image:: https://travis-ci.org/kecebongsoft/pykey.svg?branch=develop 
.. _ImageLink: http://travis-ci.org/kecebongsoft/pykey

.. |ImageLink2| image:: https://coveralls.io/repos/kecebongsoft/pykey/badge.png
.. _ImageLink2: https://coveralls.io/r/kecebongsoft/pykey

pykey
------

pykey is a credential management tool to store private information. For
now it works only for password, but its implementation is designed to
move towards more than just password, such as credit cards, or any other
credentials (string) that needs to be encrypted. All pykey data is
stored in your local computer and you can configure its path as you like. 

How to use pykey
==================

First you will need to setup your default vault. Pykey vault is
basically a JSON file where pykey stores all your password
encrypted using AES256. To unlock the vault, you will need to have
passphrase-protected private key.

You can use this default vault to store all your passwords.  
If you'd like to separate between personal and work passwords, 
such as your personal email and your work email, you can create
a separate vault later on. To setup a default vault, use the following
command::

    pykey

This will find the default vault and if you don't have any yet, it will
create a new one and prompt you this::

    Default vault not found, it seems like you are running this command 
    for the first time. Let's create a default vault for you.
    Enter your key (Something you can easily remember but secure enough): ilovefish
    Confirm your key: ilovefish

That's it you are ready to use pykey!. To create a new password, use
this command::

    >> pykey new
    Enter key for default vault: ilovefish
    Enter the name for this credential: My personal email
    Enter username used in the service: fishlover@gmail.com
    How lengthy the password will be [15]: 
    Include non-alphanumeric [Y/n]: 
    Shortcode (max-3 chars) []: pe
    Password created for "My personal email" with shortcode pe.

The last bit, is an optional shortcode for you to easily access
frequently used password. To edit existing passwords, use the followng
command::

    >> pykey edit pe
    Enter key for default vault: ilovefish
    Enter the name for this credential [My personal email]: 
    Enter username used in the service [fishlover@gmail.com]:
    How lengthy the password will be [15]: 
    Include non-alphanumeric [Y/n]: 
    Shortcode (max-3 chars) [pe]: 
    Password updated for "My personal email" with shortcode pe.

What if you don't want your password to be auto-generated?, you can pass
the ``--no-gen`` parameter when creating/editing password::

    >> pykey edit pe --no-gen
    Enter key for default vault: ilovefish
    Enter the name for this credential [My personal email]: 
    Enter username used in the service [fishlover@gmail.com]:
    Enter the password: iloveturtlesmore
    Confirm the password: iloveturtlesmore
    Shortcode (max-3 chars) [pe]: 

To list your passwords, use::

    >> pykey
    Enter key for default vault: ilovefish

    ======================================================================================================
    Code| # | Name                      | Username              | Created             | Modified
    ======================================================================================================
        | 1 | My Facebook               | fishlover             | 1 Jan 2014 03:30 PM | 1 May 2014 10:00AM
        | 2 | My Twitter                | fishlover             | 1 Jan 2014 03:30 PM | 1 May 2014 10:00AM
        | 3 | Personal email at yahoo   | fish_lover@yahoo.com  | 1 Jan 2014 03:30 PM | 1 May 2014 10:00AM
    pe  | 4 | My personal email         | fishlover@gmail.com   | 1 Jan 2014 03:30 PM | 1 May 2014 10:00AM
    ins | 5 | Instagram                 | fishlover             | 1 Jan 2014 03:30 PM | 1 May 2014 10:00AM
    ======================================================================================================

You can also find by using the ``find`` command::

    >> pykey find personal
    Enter key for default vault: ilovefish

    ======================================================================================================
    Code| # | Name                      | Username              | Created             | Modified
    ======================================================================================================
        | 3 | Personal email at yahoo   | fish_lover@yahoo.com  | 1 Jan 2014 03:30 PM | 1 May 2014 10:00AM
    pe  | 4 | My personal email         | fishlover@gmail.com   | 1 Jan 2014 03:30 PM | 1 May 2014 10:00AM
    ======================================================================================================

You can then use the shortcode or ID to fetch the password::

    >> pykey get 1
    Enter key for default vault: ilovefish
    Copied "My facebook" password to clipboard

    >> pykey get pe
    Enter key for default vault: ilovefish
    Copied "My personal email" password to clipboard

The default behaviour is to copy the password to your clipboard. You can
also choose to just show it in terminal::

    >> pykey get pe --show
    Enter key for default vault: ilovefish
    df0098!@#39w8qe

If you wish to have another vault to store another set of passwords, you
can use this command::

    >> pykey vaults new
    Creating a new vault.
    Enter a unique vault name: work
    Enter your key (Something you can easily remember but secure enough): ihatemonday
    Confirm your key: ihatemonday

After that, you can start to create, edit, list and find passwords as
demonstrated above with your new vault, just pass the ``-v`` parameter::

    >> pykey -v work

To list all registered vaults, use::

    >> pykey vaults
    1. Default
    2. work

To edit the vault passphrase, use::

    >> pykey vaults edit 2
    Editing vault "work"
    Enter your key (Something you can easily remember but secure enough): ilovefriday
    Confirm your key: ilovefriday

Configuring pykey
==================
By default, pykey stores all keys and vaults in ``~/.pykey``, and 
configuration is in ``~/.pykeyrc``. You can move pykey storages and even
separate the vaults and keys by modifying ``~/.pykeyrc`` file::

    [default]
    key = ~/.pykey/default.key
    vault = ~/.pykey/default.json

    [work]
    key = ~/Dropbox/pykey-work.key
    vault = ~/Google Drive/pykey-vault.json

FAQ
----

What is the security measurement applied in pykey?
===================================================

Pykey is using AES-256 encryption to encrypt your keys. All the values stored
in the vault are encrypted using your keys.

What if someone hack into my laptop and steal my vault and key file?
=====================================================================
He can have your vault and key file, but as long as he didn't know your
passphrase for the key, he will not be able to decrypt your vault (and
see your passwords). He will be able to browse inside the vault since 
it's a normal JSON file, but all he can see is some encrypted values for 
your password name, password value, shortcode and everything else.

What if I lost my vault and/or key file?
=================================================
I'm sorry but you'll be screwed. I recommend you to have a master
account, such as a GMail account, where you can use it to register to 
all sorts of services (Facebook, Twitter, Amazon, etc). You can use pykey for 
all accounts including GMail, and link your GMail account to your 
phone number (and verify it).

When you lost your vault/key file, you can then reset your GMail
password via phone, and begin resetting your passwords for the rest of
your accounts.

In real practice, this should **rarely** happen. Although you may lose it
when:

    * You accidentally delete the file.
    * Your computer is corrupted and you have no choice but to
      reinstall/format it.
    * Some virus (I doubt it).
    * You lose your laptop.

Hence it's recommended to store your vault & key file in some storage
services which linked to your Gmail (so you can retreive it later).
Please check at the configuration section above on how you can modify
the vault & key path. You can use Dropbox, Google Drive, or anything
else.

Does pykey protects the password on my clipboard?
=========================================================
Currently, no. I don't think any password manager can conceal the
clipboard values. You will have to make sure there's no malware sniffing
your clipboard. I believe no password manager can protect you if you
already have something malicious in your computer, cmiiw. Use antivirus
for that.

Will pykey have desktop and/or mobile apps?
==================================================
Yes, I am currently looking for frameworks to make it easy for
desktop/mobile app development. Mac will be the first target.

How can I contribute?
===============================
Thanks! pykey is currently in the very early stage and need a lot of
inputs, especially in terms of security measurement. Please read through
this readme and post any issue you have in mind.
