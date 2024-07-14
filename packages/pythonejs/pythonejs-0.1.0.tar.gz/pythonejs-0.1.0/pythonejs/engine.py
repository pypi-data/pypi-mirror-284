import re
import os

class EjsTemplateEngine:
    def __init__(self, template_dir):
        self.template_dir = template_dir
        self.code_pattern = re.compile(r'<%([\s\S]+?)%>')
        self.output_pattern = re.compile(r'<%=([\s\S]+?)%>')
        self.include_pattern = re.compile(r'<%\s*include\s+([\w\.]+)\s*%>')
        self.block_pattern = re.compile(r'<%\s*block\s+(\w+)\s*%>([\s\S]+?)<%\s*endblock\s*%>')
        self.extend_pattern = re.compile(r'<%\s*extends\s+([\w\.]+)\s*%>')
        self.blocks = {}

    def read_template(self, template_name):
        path = os.path.join(self.template_dir, template_name)
        with open(path, 'r') as file:
            return file.read()

    def parse_template(self, template_string):
        code_blocks = self.code_pattern.findall(template_string)
        output_blocks = self.output_pattern.findall(template_string)
        return code_blocks, output_blocks

    def render_template(self, template_name, context):
        template_string = self.read_template(template_name)

        # Handle inheritance
        parent_match = self.extend_pattern.search(template_string)
        if parent_match:
            parent_template_name = parent_match.group(1).strip()
            parent_template_string = self.read_template(parent_template_name)
            self.extract_blocks(template_string)
            template_string = self.replace_blocks(parent_template_string)

        # Handle includes
        template_string = self.include_pattern.sub(lambda match: self.render_template(match.group(1).strip(), context), template_string)

        def execute_code(match):
            code = match.group(1).strip()
            exec(code, context)
            return ''

        def evaluate_expression(match):
            expression = match.group(1).strip()
            return str(eval(expression, context))

        template_string = self.code_pattern.sub(execute_code, template_string)
        template_string = self.output_pattern.sub(evaluate_expression, template_string)

        return template_string

    def extract_blocks(self, template_string):
        for match in self.block_pattern.finditer(template_string):
            block_name = match.group(1).strip()
            block_content = match.group(2).strip()
            self.blocks[block_name] = block_content

    def replace_blocks(self, parent_template_string):
        def replace_block(match):
            block_name = match.group(1).strip()
            if block_name in self.blocks:
                return self.blocks[block_name]
            return match.group(2).strip()

        return self.block_pattern.sub(replace_block, parent_template_string)
