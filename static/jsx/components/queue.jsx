import React from 'react';

class Queue extends React.Component {

    constructor() {
        super();

        this.retrieveMusicQueue = this.retrieveMusicQueue.bind(this);

        this.state = {
            musicQueue: []
        };
    }

    componentDidMount() {
        this.retrieveMusicQueue();
        this.polling = setInterval(() => {
            this.retrieveMusicQueue();
        }, 5000);
    }

    componentWillUnmount() {
        clearInterval(this.polling);
    }

    retrieveMusicQueue() {
        fetch('/api/songs')
            .then((r) => {
                return r.json();
            })
            .then((response) => {                
                this.setState({
                    musicQueue: response.song_list 
                });                
            });
    }

    render() {
                
        if (this.state.musicQueue.length === 0) {
            return (<div className="text-center">
                <div className="musicList-error--empty">Looks like no music has been queued, why not be the first?</div>
            </div>);    
        }

        return (<div className="text-center">
                    <h3>Music Queue</h3>
                    <div className="col-sm-6 col-sm-offset-3">
                        <ol>
                        {
                            this.state.musicQueue.map(item => {
                                return (<li className="musicItem-list">{item}</li>);
                            })
                        }
                        </ol>
                    </div>
                </div>);
    }

    
}    

export default Queue;