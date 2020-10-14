import React, { Component } from 'react';
import TestItem from './TestItem';
import PropTypes from 'prop-types';

class TestComponent extends Component {
    render() {
        return this.props.testcomponent.map((eachtest) => (
            <TestItem
                key={eachtest.id}
                eachtest={eachtest}
                markComplete={this.props.markComplete}
                deleteTest={this.props.deleteTest}
            />
        ));
    }
}

// Prop Types:
TestComponent.prop_types = {
    tests: PropTypes.array.isRequired
}

export default TestComponent;
