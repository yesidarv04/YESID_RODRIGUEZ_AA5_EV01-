from flask import Blueprint, render_template, request, jsonify

# Creación de un Blueprint para la autenticación
auth_bp = Blueprint('auth', __name__)

# Lista para almacenar registros de usuarios y contraseñas
users = []

# Ruta para el registro de usuarios
@auth_bp.route('/registro', methods=['POST'])
def registro():
    # Obtener los datos del formulario de registro
    usuario = request.json.get('usuario')
    contraseña = request.json.get('contraseña')
    
    # Verificar si el usuario ya está registrado
    for user in users:
        if user['usuario'] == usuario:
            return jsonify({'error': 'Usuario ya registrado'}), 401
    
    # Agregar el nuevo usuario a la lista
    users.append({'usuario': usuario, 'contraseña': contraseña})
    return jsonify({'mensaje': 'Registro exitoso'})

# Ruta para el inicio de sesión
@auth_bp.route('/inicio_sesion', methods=['POST'])
def inicio_sesion():
    # Obtener los datos del formulario de inicio de sesión
    usuario = request.json.get('usuario')
    contraseña = request.json.get('contraseña')
    
    # Verificar si el usuario y la contraseña coinciden con los registros
    for user in users:
        if user['usuario'] == usuario and user['contraseña'] == contraseña:
            return jsonify({'mensaje': 'Autenticación exitosa'})
    
    # Si las credenciales no son válidas, devolver un código de estado 401 (Unauthorized)
    return jsonify({'error': 'Error en la autenticación'}), 401

# Ruta para mostrar el formulario de registro
@auth_bp.route('/registro_page', methods=['GET'])
def registro_page():
    return render_template('registro.html')

# Ruta para mostrar el formulario de inicio de sesión
@auth_bp.route('/inicio_sesion_page', methods=['GET'])
def inicio_sesion_page():
    return render_template('inicio_sesion.html')
