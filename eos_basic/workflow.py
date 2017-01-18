#    Copyright © 2017  RunasSudo (Yingtong Li)
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.

import eos_core.workflow

class TaskSetElectionDetails(eos_core.workflow.WorkflowTask):
	class EosMeta:
		eos_name = 'eos_basic.workflow.TaskSetElectionDetails'
	
	def serialise(self, hashed=False):
		return None
	
	@staticmethod
	def _deserialise(cls, value):
		return cls()

class TaskCastVotes(eos_core.workflow.WorkflowTask):
	class EosMeta:
		eos_name = 'eos_basic.workflow.TaskCastVotes'
	
	workflow_depends = ['eos_basic.workflow.TaskSetElectionDetails']
	
	def serialise(self, hashed=False):
		return None
	
	@staticmethod
	def _deserialise(cls, value):
		return cls()
