import React, { Component } from 'react';
import PropTypes from 'prop-types';

export class TestItem extends Component {
    getStyle = () => {
        /*
        if (this.props.eachtest.completed) {
            return {
                backgroundColor: '#f4f4f4',
                padding: '10px',
                textDecoration: 'line-through'
            }
        } else {
            return {
                backgroundColor: '#f4f4f4',
                padding: '10px',
                textDecoration: 'none'
            }
        }
        *//* This also can be written that way: */
        return {
            backgroundColor: '#f4f4f4',
            padding: '10px',
            borderBottom: '1px #ccc dotted',
            textDecoration: this.props.eachtest.completed ? 'line-through' : 'none'
        }
    }

    render() {
        const { id, title } = this.props.eachtest;

        return (
            // Some forms to write the same thing:
            //<div style={ itemStyle }>
            //<div style={{ backgroundColor: '#f4f4f4' }}>
            <div style={this.getStyle()}>
                <input
                    type="checkbox"
                    style={{ marginRight: '5px' }}
                    onChange={this.props.markComplete.bind(this, id)}>
                </input>

                {title}

                <button
                    onClick={this.props.deleteTest.bind(this, id)}
                    style={btnStyle}>
                    X
                </button>
            </div>
        )
    }
}

// Prop Types:
TestItem.prop_types = {
    test: PropTypes.object.isRequired
}

const btnStyle = {
    backgroundColor: '#ff0000',
    color: '#fff',
    border: 'none',
    padding: '5px 9px',
    borderRadius: '50%',
    cursor: 'pointer',
    float: 'right'
}

const itemStyle = {
    backgroundColor: '#f4f4f4'
}

export default TestItem
