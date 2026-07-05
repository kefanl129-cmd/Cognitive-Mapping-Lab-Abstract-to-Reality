# Demo 01 · Real Numbers
# Demo 01 · 实数空间认知映射

## Algebraic Extension vs. Transcendental Extension
## 代数扩张与超越扩张

> Mathematical Structure → Physical Mapping → Scientific Visualization
>
> 数学结构 → 物理映射 → 科学可视化

---

# 项目简介 | Overview

本 Demo 是 **Cognitive Mapping Lab** 的第一个数学可视化实验。

项目尝试回答一个经典数学问题：

> 为什么代数无理数与超越数同属于无理数，却表现出完全不同的结构特征？

本项目并非重新定义数学，而是建立一种**认知映射（Cognitive Mapping）**：

将抽象数学结构映射为可视化的物理空间模型，以帮助理解不同类型实数之间的结构差异。

---

This demo is the first visualization project of the **Cognitive Mapping Lab**.

Its objective is to explore an intuitive question:

> Why do algebraic irrational numbers and transcendental numbers both belong to the irrational numbers while exhibiting fundamentally different structural behaviors?

Rather than redefining mathematics, this project proposes a **Cognitive Mapping** from abstract mathematical structures to intuitive physical-space visualizations.

---

# 一、代数扩张
# I. Algebraic Extension

## 数学本质 | Mathematical Perspective

设新引入元素

> α（如 √2、∛5）

满足

> f(α)=0

其中 f(x) 为有理系数多项式。

因此：

- 极小多项式存在；
- 扩张次数有限；
- 属于有限维向量空间；
- 具有严格的代数约束。

---

Let α (e.g. √2, ∛5) satisfy

> f(α)=0

for some polynomial over the rational field.

Therefore,

- a minimal polynomial exists;
- the extension degree is finite;
- the extension remains finite-dimensional;
- every element is algebraically constrained.

---

## 认知物理映射 | Physical Interpretation

在本项目中，

代数扩张被映射为一种：

> **全约束的刚性满铺空间（Rigid Fully-Constrained Space）**

每一个新增粒子都受到多项式约束，

空间中的每一个格点都能够被数学关系精准测度与锚定。

整个系统快速达到新的稳定闭环：

- Zero Relaxation（零松弛度）
- Complete Constraint（完全约束）
- Fully Filled Space（刚性满铺）

可以将其理解为一种受到严格规则支配的稳定结构。

---

Within this visualization,

algebraic extensions are interpreted as a

> **Rigid Fully-Constrained Space.**

Every newly introduced particle is anchored by polynomial relations.

The expanded space rapidly reaches a new algebraic equilibrium characterized by

- Zero Relaxation
- Complete Constraint
- Fully Filled Structure

---

# 二、超越扩张
# II. Transcendental Extension

## 数学本质 | Mathematical Perspective

设新引入元素

> t（如 π、e）

满足

> 对任意有理系数多项式，

> f(t) ≠ 0

因此，

不存在有限阶代数关系。

系统必须容纳

> 1,t,t²,t³,...

空间提升为可数无限维。

---

Let t (e.g. π or e) satisfy

> f(t) ≠ 0

for every polynomial over the rational field.

No finite algebraic relation exists.

The basis necessarily expands into

> 1,t,t²,t³,...

leading to an infinite-dimensional extension.

---

## 认知物理映射 | Physical Interpretation

本项目将超越扩张映射为：

> **无限维自由流体（Infinite-Dimensional Free Fluid）**

由于摆脱全部代数约束，

粒子拥有最大的自由度。

系统表现出：

- Infinite Degrees of Freedom（无限自由度）
- Positive Relaxation（正松弛度）
- Continuous Expansion（持续扩张）

空间始终保持开放，

不存在有限边界能够完全约束其演化。

---

Within this project,

transcendental extensions are visualized as an

> **Infinite-Dimensional Free Fluid.**

Freed from every finite algebraic constraint,

particles exhibit maximal freedom,

continuous expansion,

and an intrinsically open spatial structure.

---

# 数学世界观
# Mathematical Worldview

本项目提出一种认知映射：

## 有理数（Rational Numbers）

代表数学空间的钢筋骨架。

特点：

- 可数
- 离散
- 运算闭环
- 精确坐标

它们构成整个数学结构的基础框架。

---

Rational numbers form the structural skeleton of mathematical space,

providing

- countability,
- discreteness,
- algebraic closure,
- precise coordinates.

---

## 代数无理数（Algebraic Irrational Numbers）

代数无理数依附于多项式约束，

如同刚性填充材料，

与有理数共同构建稳定连续空间。

---

Algebraic irrational numbers remain attached to polynomial constraints,

acting as rigid fillers within the mathematical structure.

---

## 超越数（Transcendental Numbers）

超越数摆脱了所有有限代数关系。

在测度意义下，

几乎所有实数都是超越数。

因此，

它们代表连续统中最自由、最丰富的组成部分。

在本项目中，

这种性质被映射为一种具有无限自由度的连续流体。

---

Transcendental numbers satisfy no finite polynomial relation.

From the viewpoint of measure theory,

they occupy almost every point of the real line.

Within this visualization,

they are represented as an infinitely free continuous fluid.

---

# 可视化内容
# Visualization Components

本 Demo 包括：

- 有理数网格
- 实数球面
- 代数粒子轨迹
- 超越数轨迹
- 动态尾迹
- 流体粒子系统
- 三维相机旋转
- 信息面板

全部动画均基于

- Python
- NumPy
- Matplotlib

生成。

---

This visualization includes

- Rational Grid
- Real Sphere
- Algebraic Particles
- Transcendental Trajectories
- Dynamic Tail
- Particle Flow
- Camera Rotation
- Information Panel

implemented with

- Python
- NumPy
- Matplotlib

---

# 项目定位
# Project Position

```
抽象数学
(Abstract Mathematics)

        ↓

数学结构分析
(Mathematical Structures)

        ↓

认知物理映射
(Cognitive Physical Mapping)

        ↓

科学可视化
(Scientific Visualization)

        ↓

计算建模
(Computational Modeling)

        ↓

人工智能教育
(Interactive AI Education)
```

---

## License

MIT License

---

**Cognitive Mapping Lab**

Exploring Mathematics through Scientific Visualization.
