var Status = Vue.component("Home", {
    template: `
    <div class="container justify-content-between flex-wrap flex-md-nowrap align-items-center pt-3 pb-2 mb-3 border-bottom" id="status">

        <h1 class="h2">Status</h1>
        <span v-if="!status">Loading</span>

        <div class="row">
        
            <div class="col-xl-6">
                <div class="card">
                    <div class="card-header">
                        <b>System Status</b>
                    </div>
                    <div class="card-body">
                        <table class="table table-sm table-hover">
                            <tbody>
                                <tr>
                                    <td>Dicom Listener</td>
                                    <td>
                                        <span class="badge badge-success" v-if="status.dicom_listener.listening">OK</span>
                                        <span class="badge badge-danger"
                                            v-if="!status.dicom_listener.listening">Stopped</span>
                                        <br><span>Port: <b>{{status.dicom_listener.port}}</b></span>
                                        <br><span>AE Title: <b>{{status.dicom_listener.aetitle}}</b></span>
                                    </td>
                                </tr>
                                <tr>
                                    <td>Current CPU Usage</td>
                                    <td>{{ status.cpu_usage }}%</td>
                                </tr>
                                <tr>
                                    <td>Current RAM Usage</td>
                                    <td>{{ status.ram_usage.free | toGB }}/{{ status.ram_usage.total | toGB }}GB</td>
                                </tr>
                                <tr>
                                    <td>Current HD Usage</td>
                                    <td>{{ status.disk_usage.free | toGB }}/{{ status.disk_usage.total | toGB }}GB</td>
                                </tr>
                            </tbody>
                        </table>
                    </div>
                </div>
            </div>
            <div class="col-xl-6">
                <div class="card">
                    <div class="card-header">
                        <b>Algorithms Available</b>
                    </div>
                    <div class="card-body" v-for="a in status.algorithms">
                        <table class="table table-sm table-hover">

                            <thead>
                                <b>{{a.name}}</b>
                            </thead>
                            <tbody>
                                <tr>
                                    <td>Default Settings:</td>
                                    <td>
                                        <pre>{{JSON.stringify(a.default_settings, null, '    ') }}</pre>
                                    </td>
                                </tr>
                            </tbody>
                        </table>
                    </div>
                </div>
            </div>
        </div>
        <div class="row" v-if="status.applications">
            <div class="col-xl-6">
                <div class="card">
                    <div class="card-header">
                        <b>Applications</b>
                    </div>
                    <div class="card-body">
                        <table class="table table-sm table-hover">
                            <thead>
                                <tr>
                                    <th>Name</th>
                                    <th>API Key</th>
                                </tr>
                            </thead>
                            <tbody>
                                <tr v-for="a in status.applications">
                                    <td>{{a.name}}</td>
                                    <td>{{a.key}}</td>
                                </tr>
                            </tbody>
                        </table>
                    </div>
                </div>
            </div>
        </div>
    </div>
  `,
    data: function () {
      return {
        status: {},
        timer: ""
      }
    },
    filters: {
        toGB: function (value) {
            if (typeof value !== "number") {
                return value;
            }
            var kb = value / 1024;
            var mb = kb / 1024;
            var gb = mb / 1024;
            return Math.round(gb * 100) / 100;
        }
      },
    // define methods under the `methods` object
    methods: {
        fetch: function (event) {

            this.$http.get('/status').then(response => {

                console.log(response);

                // get the Status URL
                this.status = response.body;

            }, response => {
                // error callback
                console.log(response.body);
            });
        },
        cancelAutoUpdate: function () {
            clearInterval(this.timer);
        }
    },
    beforeDestroy() {
        clearInterval(this.timer)
    },
    beforeMount() {
        this.fetch();
        this.timer = setInterval(this.fetch, 10000);
    }
});