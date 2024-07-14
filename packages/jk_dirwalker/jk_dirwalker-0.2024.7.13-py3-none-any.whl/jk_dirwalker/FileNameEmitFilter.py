


import os
import typing

import jk_typing

from .DirEntryX import DirEntryX
from .StdEmitFilter import StdEmitFilter





#
# This emit filter will return only regular files that have one of the specified file extensions.
#
class FileNameEmitFilter(StdEmitFilter):

	def __init__(self, *fileNames):
		super().__init__(
			emitWalkRoot=False,
			emitDirectories=False,
			emitRegularFiles=True,
			emitSymLinks=False,
			emitBlockDevices=False,
			emitCharacterDevices=False,
			emitSockets=False,
			emitFIFOs=False,
			emitOthers=False,
			emitErrors=True,
		)

		self.__fileNames = []
		for fileName in fileNames:
			assert isinstance(fileName, str)
			assert fileName
			self.__fileNames.append(fileName)
	#

	def checkEmit(self, entry:DirEntryX) -> bool:
		b = super().checkEmit(entry)
		if not b:
			return False

		for fileName in self.__fileNames:
			if entry.name == fileName:
				return True

		return False
	#

#



