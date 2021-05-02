using UnityEngine;
using UnityEditor;
using System.Reflection;

//https://bitbucket.org/snippets/pschraut/8ex498

[CanEditMultipleObjects]
[CustomEditor(typeof(Transform))]
public class EditorResetTransformButton : Editor
{
    private SerializedProperty mLocalPosition;
    private SerializedProperty mLocalRotation;
    private SerializedProperty mLocalScale;

    private object mTransformRotationGUI;

    private void OnEnable() 
    {
        if(null == serializedObject)
            return;

        mLocalPosition      = serializedObject.FindProperty("m_LocalPosition");
        mLocalRotation      = serializedObject.FindProperty("m_LocalRotation");
        mLocalScale         = serializedObject.FindProperty("m_LocalScale");

        if(null == mTransformRotationGUI)
            mTransformRotationGUI = System.Activator.CreateInstance(typeof(SerializedProperty).Assembly.GetType("UnityEditor.TransformRotationGUI", false, false));
        
         mTransformRotationGUI.GetType().GetMethod("OnEnable").Invoke(mTransformRotationGUI, new object[] { mLocalRotation, new GUIContent("Rotation") });
    }

        public override void OnInspectorGUI()
        {
            var serObj = this.serializedObject;
            if (serObj == null)
                return;

            serObj.Update();

            DrawLocalPosition();
            DrawLocalRotation();
            DrawLocalScale();

            DrawPropertiesExcluding(serObj, new string[] { "m_LocalPosition", "m_LocalRotation", "m_LocalScale" });

            Verify();

            serObj.ApplyModifiedProperties();
        }

        void DrawLocalPosition()
        {
            using (new EditorGUILayout.HorizontalScope())
            {
                if (GUILayout.Button(new GUIContent("P", "Reset Position"), EditorStyles.miniButton, GUILayout.Width(20)))
                    mLocalPosition.vector3Value = Vector3.zero;

                EditorGUILayout.PropertyField(mLocalPosition, new GUIContent("Position"));
            }
        }

        void DrawLocalRotation()
        {
            using (new EditorGUILayout.HorizontalScope())
            {
                if (GUILayout.Button(new GUIContent("R", "Reset Rotation"), EditorStyles.miniButton, GUILayout.Width(20)))
                    mLocalRotation.quaternionValue = Quaternion.identity;

                mTransformRotationGUI.GetType().GetMethod("RotationField", BindingFlags.Instance | BindingFlags.Public | BindingFlags.NonPublic, null, new[] { typeof(bool) }, null).Invoke(mTransformRotationGUI, new object[] { false });                
            }
        }

        void DrawLocalScale()
        {
            using (new EditorGUILayout.HorizontalScope())
            {
                if (GUILayout.Button(new GUIContent("S", "Reset Scale"), EditorStyles.miniButton, GUILayout.Width(20)))
                    mLocalScale.vector3Value = Vector3.one;

                EditorGUILayout.PropertyField(mLocalScale, new GUIContent("Scale"));
            }
        }

        void Verify()
        {
            var transform = target as Transform;
            var position = transform.position;
            if (Mathf.Abs(position.x) > 100000f || Mathf.Abs(position.y) > 100000f || Mathf.Abs(position.z) > 100000f)
                EditorGUILayout.HelpBox("Due to floating-point precision limitations, it is recommended to bring the world coordinates of the GameObject within a smaller range.", MessageType.Warning);
        }
}
