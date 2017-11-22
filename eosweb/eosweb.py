#   Eos - Verifiable elections
#   Copyright © 2017  RunasSudo (Yingtong Li)
#
#   This program is free software: you can redistribute it and/or modify
#   it under the terms of the GNU Affero General Public License as published by
#   the Free Software Foundation, either version 3 of the License, or
#   (at your option) any later version.
#
#   This program is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU Affero General Public License for more details.
#
#   You should have received a copy of the GNU Affero General Public License
#   along with this program.  If not, see <http://www.gnu.org/licenses/>.

import click
import flask

app = flask.Flask(__name__)

@app.cli.command('test')
@click.option('--prefix', default=None)
@click.option('--lang', default=None)
def run_tests(prefix, lang):
	import eos.tests
	eos.tests.run_tests(prefix, lang)

@app.route('/')
def index():
	return flask.render_template('index.html')