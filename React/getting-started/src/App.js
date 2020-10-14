import React, { Component } from 'react';
import { BrowserRouter as Router, Route } from 'react-router-dom';
import axios from 'axios';

import TestComponent from './components/TestComponent';
import Header from './components/layout/Header';
import About from './components/pages/About';

import './App.css';

class App extends Component {
  state = {
    testcomponent: []
  }

  markComplete = (id) => {
    this.setState({
      testcomponent: this.state.testcomponent.map(
        test => {
          if (test.id === id) {
            test.completed = !test.completed;
          }

          return test;
        }
      )
    })
  }

  deleteTest = (id) => {
    this.setState(
      {
        testcomponent: [...this.state.testcomponent.filter(
          test => test.id !== id
        )]
      });
  }

  // Life Cycle Method - Component Did Mount:
  componentDidMount() {
    axios.get('https://jsonplaceholder.typicode.com/todos').then(
      response => this.setState({ testcomponent: response.data })
    )
  }

  // Life Cycle Method - Render:
  render() {
    return (
      <Router>
        <div className="App" >
          <Header />
          <Route exact path="/" render={props => (
            <React.Fragment>
              <TestComponent
                testcomponent={this.state.testcomponent}
                markComplete={this.markComplete}
                deleteTest={this.deleteTest}
              />
            </React.Fragment>)}
          />
          <Route path="/about" component={About} />
        </div>
      </Router>
    );
  }
}

export default App;
