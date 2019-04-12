Setting up Pickit with Siemens PLC
===================================

This manual explains how to make Pickit communicate with a Siemens PLC.
This manual guides you through the process in TIA-portal. The files are
however also compatible with Siematic manager (S7).

Step 1: Check the hardware configuration
----------------------------------------

Make sure that both the PLC is equipped with a ProfiNET or
TCP/IP-connector and that both the PLC as well as Pickit are connected
to the network. Pickit communicates with the robot (or in this case
PLC) with the TCP/IP-protocol. For an in-depth specification about this
low-level communication structure, this 
`link <https://support.pickit3d.com/article/51-the-low-level-communication-structures-between-a-robot-and-pick-it-on-the-tcp-ip-socket-level>`__
will be useful. Unlike a lot of 

**Q: Welk object is Pickit in de network?**

**Q: Vraag Jan foto netwerk setup in TIA**

Step 2: Download the necessary files
------------------------------------

Pickit provides a function block and additional data blocks for
communication over TCP/IP. The necessary (.scl) file can be found in the
table below. Make sure to choose the correct PLC version.

S300/S400/S1200/S1500

**Q: Vraag Jan?**

3: Migration of Pickit function blocks
---------------------------------------

The first step consists in adding the downloaded file in your TIA-portal
project. This is done by clicking on add new external file within the
project tree. After the .scl is added, generate the functionblock from
source using right-click.

Step 4: Add the function block to your project
----------------------------------------------

From step 2, a new function block called CommunicationPickit\_SCL should
be available in the active project tree under program blocks. Drag this
block into the desired location of your project. Within this tutorial,
we simply drag it into our main OB1. TIA-portal
automatically generates the necessary datablock which has to be
confirmed in the dialog.

The Pickit function block contains inputs and outputs. Firstly, the
inputs are discussed. The inputs contain the information sent to Pickit
during communication. This information exists of the actual robot
position, some basic commando’s seen in the `cheat
sheet <https://support.pickit3d.com/article/50-the-pick-it-functions-cheat-sheet>`__,
and the Pickit IP and Port data.

**Q: Should be robot pose be multiplied with MULT (10000) in advance?
Q: If both Successfull and Not Successfull false then ????
Q:Typo Jan Successfull ???? **

+--------------+--------------+--------------+--------------+--------------+--------------+
| **Input**    | **Type**     | **Descriptio | **Output**   | **Type**     | **Descriptio |
|              |              | n**          |              |              | n**          |
+--------------+--------------+--------------+--------------+--------------+--------------+
| ActualPosX   | Byte[4]      | The actual   | Connected    | Bool         | Is there a   |
|              |              | robot        |              |              | stable       |
|              |              | position in  |              |              | connection   |
|              |              | X            |              |              | between      |
|              |              |              |              |              | Pickit and  |
|              |              |              |              |              | the PLC      |
+--------------+--------------+--------------+--------------+--------------+--------------+
| ActualPosY   | Byte[4]      | The actual   | Waiting      | Bool         | TRUE if      |
|              |              | robot        |              |              | message is   |
|              |              | position in  |              |              | sent and     |
|              |              | Y            |              |              | waiting for  |
|              |              |              |              |              | response.    |
+--------------+--------------+--------------+--------------+--------------+--------------+
| ActualPosZ   | Byte[4]      | The actual   | Successful   | Bool         | TRUE if      |
|              |              | robot        |              |              | Pickit      |
|              |              | position in  |              |              | processed    |
|              |              | Z            |              |              | the message  |
|              |              |              |              |              | successfully |
|              |              |              |              |              | .            |
+--------------+--------------+--------------+--------------+--------------+--------------+
| ActualPosA   | Byte[4]      | The actual   | Not          | Bool         | TRUE if      |
|              |              | robot        | Successful   |              | Pickit      |
|              |              | orientation  |              |              | processed    |
|              |              | A.\*         |              |              | the message  |
|              |              |              |              |              | not          |
|              |              |              |              |              | successfully |
|              |              |              |              |              | .            |
+--------------+--------------+--------------+--------------+--------------+--------------+
| ActualPosB   | Byte[4]      | The actual   | ObjectPosX   | Real         | The latest   |
|              |              | robot        |              |              | returned     |
|              |              | orientation  |              |              | object       |
|              |              | B.\*         |              |              | position X.  |
+--------------+--------------+--------------+--------------+--------------+--------------+
| ActualPosC   | Byte[4]      | The actual   | ObjectPosY   | Real         | The latest   |
|              |              | robot        |              |              | returned     |
|              |              | orientation  |              |              | object       |
|              |              | C.\*         |              |              | position Y.  |
+--------------+--------------+--------------+--------------+--------------+--------------+
| ActualPosD   | Byte[4]      | The actual   | ObjectPosZ   | Real         | The latest   |
|              |              | robot        |              |              | returned     |
|              |              | orientation  |              |              | object       |
|              |              | D.\*         |              |              | position Z.  |
+--------------+--------------+--------------+--------------+--------------+--------------+
| pickit\_find | Bool         | Pickit      | ObjectPosA   | Real         | The latest   |
| \_calib\_pla |              | command for  |              |              | returned     |
| te           |              | searching    |              |              | object       |
|              |              | the          |              |              | orientation  |
|              |              | calibration  |              |              | A.\*         |
|              |              | plate (see   |              |              |              |
|              |              | `cheat       |              |              |              |
|              |              | sheet <https |              |              |              |
|              |              | ://support.p |              |              |              |
|              |              | ickit3d.com/ |              |              |              |
|              |              | article/50-t |              |              |              |
|              |              | he-pick-it-f |              |              |              |
|              |              | unctions-che |              |              |              |
|              |              | at-sheet>`__ |              |              |              |
|              |              | ).           |              |              |              |
+--------------+--------------+--------------+--------------+--------------+--------------+
| pickit\_look | Bool         | Pickit      | ObjectPosB   | Real         | The latest   |
| \_for\_objec |              | command for  |              |              | returned     |
| t            |              | searching    |              |              | object       |
|              |              | objects in   |              |              | orientation  |
|              |              | the scene    |              |              | B.\*         |
|              |              | (see `cheat  |              |              |              |
|              |              | sheet <https |              |              |              |
|              |              | ://support.p |              |              |              |
|              |              | ickit3d.com/ |              |              |              |
|              |              | article/50-t |              |              |              |
|              |              | he-pick-it-f |              |              |              |
|              |              | unctions-che |              |              |              |
|              |              | at-sheet>`__ |              |              |              |
|              |              | ).           |              |              |              |
+--------------+--------------+--------------+--------------+--------------+--------------+
| pickit\_next | Bool         | Pickit      | ObjectPosC   | Real         | The latest   |
| \_object     |              | command for  |              |              | returned     |
|              |              | returning    |              |              | object       |
|              |              | the next     |              |              | orientation  |
|              |              | object (see  |              |              | C.\*         |
|              |              | `cheat       |              |              |              |
|              |              | sheet <https |              |              |              |
|              |              | ://support.p |              |              |              |
|              |              | ickit3d.com/ |              |              |              |
|              |              | article/50-t |              |              |              |
|              |              | he-pick-it-f |              |              |              |
|              |              | unctions-che |              |              |              |
|              |              | at-sheet>`__ |              |              |              |
|              |              | ).           |              |              |              |
+--------------+--------------+--------------+--------------+--------------+--------------+
| pickit\_conf | Bool         | Pickit      | ObjectPosD   | Real         | The latest   |
| igure        |              | command for  |              |              | returned     |
|              |              | configuring  |              |              | object       |
|              |              | setup and    |              |              | orientation  |
|              |              | product (see |              |              | D.\*         |
|              |              | `cheat       |              |              |              |
|              |              | sheet <https |              |              |              |
|              |              | ://support.p |              |              |              |
|              |              | ickit3d.com/ |              |              |              |
|              |              | article/50-t |              |              |              |
|              |              | he-pick-it-f |              |              |              |
|              |              | unctions-che |              |              |              |
|              |              | at-sheet>`__ |              |              |              |
|              |              | ).           |              |              |              |
+--------------+--------------+--------------+--------------+--------------+--------------+
| ConfigSetup  | Int          | The Pickit  | ObjectDimHei | Real         | The latest   |
|              |              | setup file   | ght          |              | returned     |
|              |              | number.      |              |              | object       |
|              |              |              |              |              | height.      |
+--------------+--------------+--------------+--------------+--------------+--------------+
| ConfigProduc | Int          | The Pickit  | ObjectDimLen | Real         | The latest   |
| t            |              | product file | gth          |              | returned     |
|              |              | number.      |              |              | object       |
|              |              |              |              |              | length.      |
+--------------+--------------+--------------+--------------+--------------+--------------+
| RobotType    | Int          | The robot    | ObjectDimWid | Real         | The latest   |
|              |              | type number  | th           |              | returned     |
|              |              | metadata     |              |              | object       |
|              |              | (these       |              |              | width.       |
|              |              | numbers can  |              |              |              |
|              |              | be found in  |              |              |              |
|              |              | the `low     |              |              |              |
|              |              | level        |              |              |              |
|              |              | communicatio |              |              |              |
|              |              | n            |              |              |              |
|              |              | structures   |              |              |              |
|              |              | page <https: |              |              |              |
|              |              | //support.pi |              |              |              |
|              |              | ckit3d.com/a |              |              |              |
|              |              | rticle/51-th |              |              |              |
|              |              | e-low-level- |              |              |              |
|              |              | communicatio |              |              |              |
|              |              | n-structures |              |              |              |
|              |              | -between-a-r |              |              |              |
|              |              | obot-and-pic |              |              |              |
|              |              | k-it-on-the- |              |              |              |
|              |              | tcp-ip-socke |              |              |              |
|              |              | t-level>`__) |              |              |              |
|              |              | .            |              |              |              |
+--------------+--------------+--------------+--------------+--------------+--------------+
| InterfaceVer | Int          | The          |              |              |              |
| sion         |              | interface    |              |              |              |
|              |              | version      |              |              |              |
|              |              | number       |              |              |              |
|              |              | metadata     |              |              |              |
|              |              | (these       |              |              |              |
|              |              | numbers can  |              |              |              |
|              |              | be found in  |              |              |              |
|              |              | the `low     |              |              |              |
|              |              | level        |              |              |              |
|              |              | communicatio |              |              |              |
|              |              | n            |              |              |              |
|              |              | structures   |              |              |              |
|              |              | page <https: |              |              |              |
|              |              | //support.pi |              |              |              |
|              |              | ckit3d.com/a |              |              |              |
|              |              | rticle/51-th |              |              |              |
|              |              | e-low-level- |              |              |              |
|              |              | communicatio |              |              |              |
|              |              | n-structures |              |              |              |
|              |              | -between-a-r |              |              |              |
|              |              | obot-and-pic |              |              |              |
|              |              | k-it-on-the- |              |              |              |
|              |              | tcp-ip-socke |              |              |              |
|              |              | t-level>`__) |              |              |              |
|              |              | .            |              |              |              |
+--------------+--------------+--------------+--------------+--------------+--------------+
| IP\_Block1   | Int          | The IP       |              |              |              |
|              |              | number first |              |              |              |
|              |              | block.       |              |              |              |
+--------------+--------------+--------------+--------------+--------------+--------------+
| IP\_Block2   | Int          | The IP       |              |              |              |
|              |              | number       |              |              |              |
|              |              | second       |              |              |              |
|              |              | block.       |              |              |              |
+--------------+--------------+--------------+--------------+--------------+--------------+
| IP\_Block3   | Int          | The IP       |              |              |              |
|              |              | number       |              |              |              |
|              |              | second       |              |              |              |
|              |              | block.       |              |              |              |
+--------------+--------------+--------------+--------------+--------------+--------------+
| IP\_Block4   | Int          | The IP       |              |              |              |
|              |              | number       |              |              |              |
|              |              | second       |              |              |              |
|              |              | block.       |              |              |              |
+--------------+--------------+--------------+--------------+--------------+--------------+
| Port\_Block1 | Int          | The IP       |              |              |              |
|              |              | number       |              |              |              |
|              |              | second       |              |              |              |
|              |              | block.       |              |              |              |
+--------------+--------------+--------------+--------------+--------------+--------------+
| Port\_Block2 | Int          | The IP       |              |              |              |
|              |              | number       |              |              |              |
|              |              | second       |              |              |              |
|              |              | block.       |              |              |              |
+--------------+--------------+--------------+--------------+--------------+--------------+

\*The orientation description varies on the submitted robot type input.

\|Functionalities and usage
---------------------------

The PLC/Pickit configuration is always set in
Master/Slave-configuration. This implies that the PLC always starts the
communication. By changing the Pickit cheat sheet functions booleans,
the request is set. The
