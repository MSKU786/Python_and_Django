from rest_framework import serializers
from .models import Note

# Added custom validation , maniputlation and read-only fields
class NoteSerializer(serializers.ModelSerializer):
    summary = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Note
        fields = [
            "id", "title", "content", "created_at", "updated_at",
            "is_archived", "is_deleted", "summary"
        ]
        read_only_fields = ("created_at", "updated_at")

        # ----- FIELD LEVEL VALIDATION -----
    def validate_title(self, value):
        if len(value) < 3:
            raise serializers.ValidationError("Title must be at least 3 chars")
        
        if (len(value) > 200):
            raise serializers.ValidationError("Title must be less than 200 chars")
    
        return value.strip()

        # ----- OBJECT LEVEL VALIDATION -----
    def validate(self, attrs):
        if attrs.get("title") == attrs.get("content"):
            raise serializers.ValidationError(
                "Title and content cannot be identical"
            )
        return attrs

    # ----- DATA MANIPULATION BEFORE SAVE -----
    def create(self, validated_data):
        validated_data["title"] = validated_data["title"].title()  # Format title
        return super().create(validated_data)

    def update(self, instance, validated_data):
        if "title" in validated_data:
            validated_data["title"] = validated_data["title"].title()
        return super().update(instance, validated_data)

    # ----- CUSTOM READ-ONLY FIELD -----
    def get_summary(self, note):
        return note.content[:50] + "..."