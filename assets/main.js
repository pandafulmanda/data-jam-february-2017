var renderer, camera, scene, controls;

function drawData(data){
  var drawingData = processData(data.tracks);
  var routesDrawingData = processData(data.routes);
  var allData = _.mapValues(drawingData, function(data, key){
    if (routesDrawingData[key]){
      return _.concat(data, routesDrawingData[key]);
    }
    return data;
  });

  window.drawingData = drawingData;
  window.routesDrawingData = routesDrawingData;
  window.allData = allData;

  // var geometries = makeGeometry(drawingData);
  // var routes = makeGeometry(routesDrawingData);
  var allGeometries = makeGeometry(allData);


  window.allGeometries = allGeometries;

  _.each(allGeometries, function(route){
    scene.add(route);
  });

  renderer.render(scene, camera);
  window.addEventListener( 'resize', onWindowResize, false );
}

function render(){
  renderer.render(scene, camera);
}

function onWindowResize() {
  camera.aspect = window.innerWidth / window.innerHeight;
  camera.updateProjectionMatrix();
  renderer.setSize( window.innerWidth, window.innerHeight );
}

function loadData(filePath){
  return function (onFileLoaded) {
    Papa.parse(filePath, {
      download: true,
      header: true,
      dynamicTyping: true,
      complete: function(results) {
        onFileLoaded(null, results.data);
      }
    })
  }
}

function parseData(callback){
  async.parallel({
    tracks: loadData("./tracks.csv"),
    routes: loadData("./routes.csv")
  }, function(err, results){
    callback(results);
  });
}

function linearScale(value, min, max){
  return ((value * 1 - min * 1)/(max * 1 - min * 1)) * 100;
}

function processData(data){
  var lat_max = _(data).maxBy('latitude').latitude;
  var lat_min = _(data).minBy('latitude').latitude;

  var long_max = _(data).maxBy('longitude').longitude;
  var long_min = _(data).minBy('longitude').longitude;

  var elevation_max = (_(data).maxBy('altitude') || {altitude: 0}).altitude;
  var elevation_min = (_(data).minBy('altitude') || {altitude: 0}).altitude;

  var processedData =  _(data)
    .map(function(point){
      return _.defaultsDeep({
        x: linearScale(point.longitude, long_min, long_max),
        y: linearScale(point.altitude || 0, 0, elevation_max),
        z: linearScale(point.latitude, lat_min, lat_max)
      }, point);
    })
    .sortBy(['timestamp'])
    .groupBy(function(point){
      return point.flight_id;
    })
    .value();

  return processedData;
}

function intialize(){
  renderer = new THREE.WebGLRenderer();
  renderer.setSize(window.innerWidth, window.innerHeight);
  document.body.appendChild(renderer.domElement);

  camera = new THREE.PerspectiveCamera(45, window.innerWidth / window.innerHeight, 1, 500);
  camera.position.set(0, 0, 100);
  camera.lookAt(new THREE.Vector3(0, 0, 0));

  scene = new THREE.Scene();


  controls = new THREE.OrbitControls( camera, renderer.domElement );
  controls.addEventListener( 'change', render ); // remove when using animation loop
}


function makeGeometry(data){

  return _.map(data, function(route){

    var material = new THREE.LineBasicMaterial({ color: Math.random() * 0xffffff });
    var geometry = new THREE.Geometry();

    _.each(route, function(point){
      geometry.vertices.push(new THREE.Vector3(point.x, point.y, point.z));
    });
    return new THREE.Line(geometry, material);

    // var points = _.map(route, function(point){
    //   return new THREE.Vector3(point.x, point.y, point.z);
    // });

    // points.push(new THREE.Vector3(points[0].x, points[0].y, points[0].z));

    // var geometry = new THREE.ConvexGeometry( points );

    // var material = new THREE.MeshPhongMaterial( {
    //     color: 0xff0000, 
    //     shading: THREE.FlatShading
    // } );

    // return new THREE.Mesh( geometry, material );
  });
}

function run(){
  intialize();
  parseData(drawData);
}

run();